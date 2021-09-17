# PIL_Tst1.py  Last updated: 21_09_11

from PIL import Image

dir_img =  "M:/DB/Im_RGB/"
fn_img =  "bird.jpg"
path_img = dir_img + fn_img
fn_img_out =  "bird_gray.jpg"
path_img_out = dir_img + fn_img_out

img = Image.open(path_img)
#img.show()

img_gray = Image.open(path_img).convert('L')
#img_gray.show()

#img_gray.save(path_img_out)
#img_gray_r = Image.open(path_img_out)
#img_gray_r.show()

height = 50
width = 50
#img_resize = img.resize(height, width)   not work
#img_resize.show()
