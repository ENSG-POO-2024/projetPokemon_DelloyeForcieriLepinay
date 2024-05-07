# Importing Image class from PIL module
from PIL import Image

# # Setting the points for cropped image
# left = 0
# top = 0
# right = 64
# bottom = 64

# # Size of the image in pixels (size of original image)
# width, height = im.size

# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
 
# # Shows the image in image viewer
# # im1.show()
# im1.save('./Temp/face.png', 'png')

########

# Opens a image in RGB mode
im = Image.open("./data/Sprite_Opacity.png")


# for j in range(3):
#     left = 1
#     top = 64*j + j + 1
#     right = 65 
#     bottom = 64*(j+1) + j + 1
    
    
    
# face = poke.crop((0, 0, 64, 64))
# dos = poke.crop((64, 0, 128, 64))
# face.save('./Temp/face.png', 'png')
# dos.save('./Temp/dos.png', 'png')

# im1 = list_pokemon[0]
# im1.save('./Temp/face.png', 'png')

id_ = 1

def decoupage(id_):

    ID = id_-1
    left = 1 + 161*(ID//3)
    top = 1 + 65*(ID%3)
    right = left + 160
    bottom = top + 64
    
    print(left,top,right,bottom)
        
        
    # elif 16 <= id_ <= 45:
        
    # elif 16 <= id_ <= 60:
        
    # elif 16 <= id_ <= 75:
        
    # elif 16 <= id_ <= 90:
        
    # elif 16 <= id_ <= 105:
        
    # elif 16 <= id_ <= 120:
        
    poke = im.crop((left, top, right, bottom))
    
    face = poke.crop((0, 0, 64, 64))
    dos = poke.crop((64, 0, 128, 64))
    face.save('./Temp/face.png', 'png')
    dos.save('./Temp/dos.png', 'png')
    
decoupage(132)