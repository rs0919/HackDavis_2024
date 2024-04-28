from django import forms
from .models import Img, EncodedImg

class ImgForm(forms.ModelForm):

    class Meta:
        model = Img
        fields = ['img', 'secret_img']


class EncodedImgForm(forms.ModelForm):

    class Meta:
        model = EncodedImg
        fields = ['name', 'encoded_img']
