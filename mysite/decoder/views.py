from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImgToDecodeForm
from .models import ImgToDecode
# Create your views here.

def image_view(request):
    
    if request.method == 'POST':
        form = ImgToDecodeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('secret_message')
    else:
        form = ImgToDecodeForm()
    
    return render(request, 'image_to_decode_form.html', {'form': form})

def index(request):
    if request == "GET":
        return HttpResponse("placeholder text")

def secret_message_view(request):
    return HttpResponse("should be secret img or text here")