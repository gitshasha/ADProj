from django.shortcuts import render,HttpResponse,redirect
import joblib
# Create your views here.
import numpy as np
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image as image_utils
from .forms import *



def hilo(request):
    return render(request,'yo.html')



def fruitmodel(request):
    cls=joblib.load("adfruitmodal")
    image_path="F:/OneDrive/Desktop/ADproj/rotated_by_15_Screen Shot 2018-06-12 at 9.38.29 PM.png"
    image = image_utils.load_img(image_path, target_size=(224, 224))
    image = image_utils.img_to_array(image)
    image = image.reshape(1,224,224,3)
    image = preprocess_input(image)
    classes={0: 'freshapples',
 1: 'freshbanana',
 2: 'freshoranges',
 3: 'rottenapples',
 4: 'rottenbanana',
 5: 'rottenoranges'}
    a=cls.predict(image)
    print(classes[np.argmax(a)])
    return render(request,'mod.html')



def preporc(img):
    file = BytesIO(img.read())
    image = image_utils.load_img(file, target_size=(224, 224))
    image = image_utils.img_to_array(image)
    image = image.reshape(1,224,224,3)
    image = preprocess_input(image)
    return image

from io import BytesIO

# Convert the InMemoryUploadedFile to a BytesIO object


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            image = request.FILES['image']
            proc=preporc(image)
            classes={0: 'freshapples',
 1: 'freshbanana',
 2: 'freshoranges',
 3: 'rottenapples',
 4: 'rottenbanana',
 5: 'rottenoranges'}
            cls=joblib.load("adfruitmodal")
            a=cls.predict(proc)
            prediction=classes[np.argmax(a)]
            return render(request, 'mod.html', {'prediction': prediction})

            # form.save()
            return redirect('/fruit/success')
    else:
        form = HotelForm()
    return render(request, 'yo.html', {'form': form})

 
def success(request):
    return HttpResponse('successfully uploaded')