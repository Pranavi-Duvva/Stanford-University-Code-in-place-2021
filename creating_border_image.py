
"""
Creating a Black border of width 10 for an image

"""

from simpleimage import SimpleImage


def main():
    image = SimpleImage("images/simba-sq.jpg")
    image.show()

    bordered_image=add_border(image,10)
    bordered_image.show()

def add_border(original_img,border_size):

    """
    Task 1
    Creating a blank image with width= 2 * border_size + original_img.width and
     height = 2 * border_size + original_img.height
    """
    new_image=SimpleImage.blank(2 * border_size + original_img.width ,2 * border_size + original_img.height )

    """
    Task 2: Creating black border
    
    """
    for y in range(new_image.height):
        for x in range(new_image.width):

            # converting all the border pixels to black

            if x  <= border_size or x >= border_size + original_img.height or y <= border_size or y >= border_size + original_img.width:

                px=new_image.get_pixel(x,y)
                px.red=0
                px.green=0
                px.blue=0

            # replacing the pixels other than the border with inage

            else:

                new_image.get_pixel(x,y).red=original_img.get_pixel(x-border_size, y-border_size).red
                new_image.get_pixel(x,y).blue = original_img.get_pixel(x - border_size, y - border_size).blue
                new_image.get_pixel(x,y).green = original_img.get_pixel(x - border_size, y - border_size).green


    return new_image






if __name__ == '__main__':
    main()