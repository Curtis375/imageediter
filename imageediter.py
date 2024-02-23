from PIL import Image, ImageEnhance, ImageFilter
import os

path ='./ims'
pathOut ='/editedIms'

for filename in os.listdir(path):
    img =Image.open(f"{path}/{filename}")


    edit = img.filter.(imagefilter.SHARPEN.convert('L').rotate(-90)

                       Factor = 1.5
                       enhancer =ImageEnhance.contrast(edit)
                       edit = enhancer.enhance(factor)

    clean_name =os.path.splittext(filename)[0]

    im_output.save(f'.{pathout}/{clean_name}_edited.jpg')

    edit.save(f'.{pathout}/{clean_name}_edited.jpg')

