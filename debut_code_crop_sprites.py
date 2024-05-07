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
im = Image.open(r"C:\projetPokemon\images\sprite_pokemons_fond_transparent.png")


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

id_ = 16
top = 1 + 65*((id_)%3) + 131*((id_)//16)

def decoupage(id_):

    if 1 <= id_ <= 15:
        left = 1 + 161*(id_//3)
        top = 1 + 65*(id_%3-1)
        right = left + 160
        bottom = top + 64
        
    elif 16 <= id_ <= 30:
        left = 1 + 161*(id_//3)
        top = 1 + 65*(id_%3-1) + 131*(id_%16-1)
        right = left + 160
        bottom = top + 64
        
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