from PIL import Image , ImageEnhance , ImageFilter
import os
 
img1 = Image.open(r'E:\testing_python\picture\background.jpg')
# image.ext changer
img1.save(r'E:\testing_python\picture\dog1.png')
img1.show()

# resizing of images
MAX_SIZE = (250,250)
img1.thumbnail(MAX_SIZE)
img1.save(r'E:\testing_python\picture\testing.jpg')

# loop for chnging ext
for item in os.listdir(r'E:\testing_python\picture'):
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        file_name,ext = os.path.splitext(item)
        img1.save(f"{file_name}.png")

# sharpness 
# 0 : bularri
# 1: orignal_img
# 2 : image_increased
#  3:
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(0).show()

# color
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(0).show()

# brightnees
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).show()

# contrest
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).show()

# bulor
img1.filter(ImageFilter.GaussianBlur(radius=8)).show()