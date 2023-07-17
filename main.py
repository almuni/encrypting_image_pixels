
from PIL import Image
import numpy as np

def scramble_pixels(image, a):
    np.random.seed(a)
    width, height = image.size
    pixels = np.array(image)
    indices = np.arange(width * height)
    np.random.shuffle(indices)
    scrambled_pixels = np.zeros_like(pixels)

    for i, index in enumerate(indices):
        x = i % width
        y = i // width
        scrambled_pixels[y, x] = pixels[index // width, index % width]

    scrambled_image = Image.fromarray(scrambled_pixels)
    return scrambled_image

def unscramble_pixels(image, a):
    np.random.seed(a)
    width, height = image.size
    pixels = np.array(image)
    indices = np.arange(width * height)
    np.random.shuffle(indices)
    unscrambled_pixels = np.zeros_like(pixels)

    for i, index in enumerate(indices):
        x = index % width
        y = index // width
        unscrambled_pixels[y, x] = pixels[i // width, i % width]

    unscrambled_image = Image.fromarray(unscrambled_pixels)
    return unscrambled_image

# Example usage
image_path = 'test.jpg'
a = int(input("Enter the value of 'a': "))

# # Scramble the pixels
original_image = Image.open(image_path)
scrambled_image = scramble_pixels(original_image, a)
scrambled_image.save('scrambled_image.jpg')
scrambled_image.show()

# Unscramble the pixels
unscrambled_image = unscramble_pixels(scrambled_image, a)
unscrambled_image.save('unscrambled_image.jpg')
unscrambled_image.show()

