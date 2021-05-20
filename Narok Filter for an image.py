
"""
Creating a Narok filter

The Narok filter replaces bright pixels in an image with gray scale value of the pixel

Gray scale value
It is the average value of Red Green Blue

Bright Pixel

If a pixel value is greater than 153 (60% of 255) it is considered a bright pixel
"""



from simpleimage import SimpleImage


Brightness_Threshold=153

def main():
    image=SimpleImage("images/simba-sq.jpg")
    image.show()

    for pixel in image:

        # calculate the average RGB

        average=(pixel.red+pixel.green+pixel.blue)//3

        if average > Brightness_Threshold:

            pixel.red=average
            pixel.green=average
            pixel.blue=average

    image.show()

if __name__ == '__main__':
    main()


