from PIL import Image
import numpy as np

# Encrypt Function
def encrypt_image(image_path, key):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encryption operation: Apply a basic manipulation (e.g., XOR with a key)
    encrypted_array = (img_array + key) % 256  # Modifying each pixel value by adding a key

    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    return encrypted_image

# Decrypt Function
def decrypt_image(encrypted_image, key):
    # Convert image to numpy array
    encrypted_array = np.array(encrypted_image)

    # Decryption operation: Reverse the encryption operation
    decrypted_array = (encrypted_array - key) % 256

    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    return decrypted_image

# Save function to handle saving
def save_image(image, path):
    image.save(path)
    print(f"Image saved at {path}")

# Example Usage
key = 50  # Encryption key
input_image_path = 'input_image.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'

# Encrypt the image
encrypted_image = encrypt_image(input_image_path, key)
save_image(encrypted_image, encrypted_image_path)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)
save_image(decrypted_image, decrypted_image_path)
