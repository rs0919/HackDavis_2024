from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImgToDecodeForm
from .models import ImgToDecode

import os

from PIL import Image
# Create your views here.

def image_view(request):
    
    if request.method == 'POST':
        form = ImgToDecodeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            source = "plain_image.png"
            for root, dirs, files in os.walk("./media/images_to_decode/"):
                for file in files:
                    if file.endswith('.png') or file.endswith('.jpg'):
                        source = str(file)
            # this code block ^ renames the image to the same thing every time

            os.rename("./media/images_to_decode/" + source, "./media/images_to_decode/encoded_image.png")
            return redirect('secret_message')
    else:
        form = ImgToDecodeForm()
    
    return render(request, 'image_to_decode_form.html', {'form': form})

def index(request):
    if request == "GET":
        return HttpResponse("placeholder text")

def secret_message_view(request):
    key = "1010101010" # change later so it's not hard coded
    secret_message = decode_img("./media/images_to_decode/encoded_image.png", key) # change
    os.system('rm -rf ./media/images_to_decode/*') # clear folder
    return HttpResponse("secret_message: " + secret_message)


def bin_to_message(binary):
    """Convert binary data to message."""
    message = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message.append(chr(int(byte, 2)))
    return ''.join(message)


def decode_img(filepath, key):
    img = Image.open(filepath)
    binary_message = ''
    width, height = img.size
    # add key to verify same group
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                binary_message += str(pixel[n] & 1 ^ int(key[len(binary_message) % len(key)], 2))
                if binary_message[-16:] == '1111111111111110':
                    return bin_to_message(binary_message[:-16])
    return "No hidden message found."