

"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():

    image = SimpleImage("images/simba-sq.jpg")


    final_image = SimpleImage.blank( WIDTH,HEIGHT)

    warhol_image(final_image,N_COLS,N_ROWS)

    final_image.show()

    # manually assigning

    row =int(input(" Enter row"))
    col=int(input("Enter col"))
    final_image_copy=final_image
    patch = make_recolored_patch(1.5,0,1.5)
    put_patch(patch, final_image_copy, col, row)

    final_image_copy.show()




def warhol_image(final_image,N_COLS,N_ROWS):

    for y in range(N_ROWS):
        for x in range(N_COLS):

            patch = make_recolored_patch(random.uniform(-0.5,1.5), random.uniform(-0.5,1.5), random.uniform(-0.5,1.5))
            put_patch(patch,final_image,x,y)






def put_patch(patch,final_image,x,y):

    patch_h =y*PATCH_SIZE
    patch_w =x*PATCH_SIZE



    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):

            pixel = patch.get_pixel(x, y)

            final_image.set_pixel(x+patch_w,y+patch_h,pixel)




def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:

        pixel.red=pixel.red * red_scale
        pixel.green=pixel.green * green_scale
        pixel.blue=pixel.blue * blue_scale
    return patch






if __name__ == '__main__':
    main()