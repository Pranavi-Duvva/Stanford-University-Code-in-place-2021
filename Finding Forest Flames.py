from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
DEFAULT_FILE = 'images/greenland-fire.png'

def main():

    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()


    #Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()





def find_flames(filename):

    image=SimpleImage(filename)

    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red >=average * INTENSITY_THRESHOLD :

            pixel.red=255
            pixel.green=0
            pixel.blue=0

        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average


    return image




def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()