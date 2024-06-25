def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    encrypted_pixels = [(pixel[0] + key, pixel[1] + key, pixel[2] + key) for pixel in pixels]
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save('encrypted_image.png')

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    decrypted_pixels = [(pixel[0] - key, pixel[1] - key, pixel[2] - key) for pixel in pixels]
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save('decrypted_image.png')