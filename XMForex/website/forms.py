from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model= Analysis
        fields= ["name", "imagefile"]

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
