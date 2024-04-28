from django import forms
from .models import ImgToDecode

class ImgToDecodeForm(forms.ModelForm):

    class Meta:
        model = ImgToDecode
        fields = ['img']