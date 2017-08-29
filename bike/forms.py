from django.forms import  ModelForm
from bike.models import Image
from django.forms import forms
class ImageForm(ModelForm):
    file = forms.FileField()
    class Meta:
        model = Image
        fields=["name","desc"]