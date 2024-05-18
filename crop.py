import os
from PIL import Image, ImageOps

imgs = []

for eachFile in os.listdir("downloads"):
    if ".jpeg" in eachFile:
        imgs.append(eachFile)
        

for eachImg in imgs:
    print("got here")
    img = Image.open(f"downloads/{eachImg}")
    img = ImageOps.crop(img, (0, 620, 0, 0))
    img.save(f"downloads/cropped/{eachImg}")
    print(f"Cropped downloads/cropped/{eachImg}")

    
    
# img = Image.open(f"downloads/1.jpeg")
# width, height = img.size
# # left, top, right, bottom
# print(height)
# img = ImageOps.crop(img, (0, 620, 0, 0))
# img.show()
