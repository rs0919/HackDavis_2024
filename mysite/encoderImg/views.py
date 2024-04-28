from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImgForm
from .models import Img, EncodedImg

import os
from PIL import Image

# Create your views here.

def index(request):
    return HttpResponse("encode your image here.")

def image_view(request):
    
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            source = "plain_image.png"
            for root, dirs, files in os.walk("./media/images/"):
                for file in files:
                    if file.endswith('.png') or file.endswith('.jpg'):
                        source = str(file)
            os.rename("./media/images/" + source, "./media/images/plain_image.png")
            # this code block ^ renames the image to the same thing every time            
            
            return redirect('images')
    else:
        form = ImgForm()

    return render(request, 'image_form.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

def encoded_image_view(request):
    if request.method == "GET":
        #Imgs = Img.objects.all()
        Imgs = (Img.objects.filter(name="plain_image")).order_by("id")
        key = "1010101010" # change later so it's not hard coded
        #new_encoded_img = encode_image("./media/images/plain_image.png", Imgs[0].secret_msg, key)
        for img in Imgs.iterator():
            new_encoded_img = encode_image("./media/images/plain_image.png", img.secret_msg, key)

        #new_encoded_img.save("newly_encoded_img.png")
        save_image(new_encoded_img, "./media/encoded_images", "newly_encoded_img.png")
        os.system('rm -rf ./media/images/*') # clear folder (not encoded img folder)
        return render(request, 'encoded_image_display.html', {'encoded_image': new_encoded_img})


def save_image(image, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    image.save(os.path.join(folder, filename))

def message_to_bin(message):
    """Convert a message to binary."""
    return ''.join(format(ord(char), '08b') for char in message)

def encode_image(file_name, message, key):
    img = Image.open(file_name)
    binary_message = message_to_bin(message) + '1111111111111110'  # Adding a delimiter
    if img.mode != 'RGB':
        img = img.convert('RGB')
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(img.getpixel((col, row)))
                for n in range(3):  # Assume RGB
                    if index < len(binary_message):
                        pixel[n] = pixel[n] & ~1 | int(binary_message[index], 2) ^ int(key[index % len(key)], 2)
                        index += 1
                encoded.putpixel((col, row), tuple(pixel))
            else:
                break
        else:
            continue
        break
    
    return encoded