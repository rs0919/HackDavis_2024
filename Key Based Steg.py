'''
The important thinkg about this script is that this is the key:
key = "1010101010"

'''


from PIL import Image
import numpy as np

def message_to_bin(message):
    """Convert a message to binary."""
    return ''.join(format(ord(char), '08b') for char in message)

def bin_to_message(binary):
    """Convert binary data to message."""
    message = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message.append(chr(int(byte, 2)))
    return ''.join(message)

def encode_image(image_path, secret_message, key):
    img = Image.open(image_path)
    binary_message = message_to_bin(secret_message)
    
    if img.mode != 'RGB':
        print("Image mode needs to be RGB")
        return False
    
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
    
    return encoded

def decode_image(image_path, key ):
    img = Image.open(image_path)
    binary_message = ''
    width, height = img.size
    
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                binary_message += str(pixel[n] & 1 ^ int(key[len(binary_message) % len(key)], 2))
    return bin_to_message(binary_message)

# Example usage:
secret_msg = "Hello, this is a secret message!"
cover_img_path = "path_to_cover_image.jpg"  # Path to your cover image
key = "1010101010"  # Unique key
encoded_image = encode_image(cover_img_path, secret_msg, key)
encoded_image.save("encoded_image.png")

decoded_message = decode_image("encoded_image.png", key)
print(decoded_message)
