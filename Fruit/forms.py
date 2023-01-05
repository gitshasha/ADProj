from django import forms
from .models import *
 
 
class HotelForm(forms.Form):
    image=forms.ImageField()
 
    # class Meta:
    #     model = Hotel
    #     fields = ['Main_Img']