from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImgToDecodeForm
from .models import ImgToDecode

from PIL import Image
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
    secret_message = decode_img("./media/images_to_decode/encoded_image.png") # change
    return HttpResponse("secret_message:" + secret_message)


def bin_to_message(binary):
    """Convert binary data to message."""
    message = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message.append(chr(int(byte, 2)))
    return ''.join(message)


def decode_img(filepath):
    img = Image.open(filepath)
    binary_message = ''
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                binary_message += str(pixel[n] & 1)
                if binary_message[-16:] == '1111111111111110':
                    return bin_to_message(binary_message[:-16])
    return "No hidden message found."