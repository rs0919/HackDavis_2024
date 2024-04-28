from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImgForm

# Create your views here.

def index(request):
    return HttpResponse("encode your image here.")

def image_view(request):
    
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('encoded_image_view')
    else:
        form = ImgForm()
    
    return render(request, 'image_form.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

def encoded_image_view(request):
    encode_image("../media/images/plain_image")
    return render(request, 'encoded_image_display.html')

def encode_image(file_name):
    return 2