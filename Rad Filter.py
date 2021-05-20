
"""
This program implements a rad image filter.

This filter replaces the Red Green Blue values of the pixel  to

new red value = old red value * 1.5
new green value = old green value * 0.7
new blue value = old blue value * 1.5
"""

from simpleimage import SimpleImage
import random

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Showing the image before the transform
    image.show()

    # Applying the filter
    new_image=code_in_place_filter('images/quad.jpg')


    # Show the image after the transform
    new_image.show()


def code_in_place_filter(filename):
    image = SimpleImage(filename)


    for pixel in image:

        pixel.red=pixel.red * 1.5
        pixel.green=pixel.green * 0.7
        pixel.blue=pixel.blue * 1.5


    return image


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()