from django import forms
from .models import User

class ManageGroupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']