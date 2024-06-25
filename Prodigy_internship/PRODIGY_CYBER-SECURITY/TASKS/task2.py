from PIL import Image

def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    encrypted_pixels = [(pixel[2], pixel[1], pixel[0]) for pixel in pixels]
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save('encrypted_image.png')

def decrypt_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    decrypted_pixels = [(pixel[2], pixel[1], pixel[0]) for pixel in pixels]
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save('decrypted_image.png')

def main():
    while True:
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            image_path = input("Enter the image path: ")
            encrypt_image(image_path)
            print("Image encrypted successfully!")
        elif choice == '2':
            image_path = input("Enter the encrypted image path: ")
            decrypt_image(image_path)
            print("Image decrypted successfully!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
    