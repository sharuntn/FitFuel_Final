from django import forms
from .models import Image
from .models import Intake

class IntakeForm(forms.ModelForm):
    class Meta:
        model = Intake
        fields = ['food_name', 'calories'] 
        
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image',)
