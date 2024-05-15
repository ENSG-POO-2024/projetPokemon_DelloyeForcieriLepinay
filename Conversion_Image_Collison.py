import numpy as np
from PIL import Image

def colormap_to_matrice(Colormap_Path, Dico):
    im = Image.open(Colormap_Path)
    x,y = im.size
    Mat = np.zeros((x,y),dtype=int)
    for x in range(0,im.size[0]):
        for y in range(0,im.size[1]):
            Mat[y,x] = Dico[im.getpixel((x,y))]
    np.savetxt("./data/Matrice2.csv", Mat, delimiter=";", fmt='%i')

Dico = {(255, 0, 0, 255):0, (255, 255, 255, 255):1, (0, 255, 164, 255):2, (0, 82, 0, 255):3, (0, 255, 0, 255): 4, (0, 0, 0, 255): 6, 
        (255, 135, 0, 255):7, (255, 0, 249, 255):8, (0, 63, 255, 255):52, (0, 255, 255, 255):51, (254, 255, 0, 255):100, (0,255,238,255):101, (255,140,249,255):102  }
colormap_to_matrice("./Map/carte2_collision_compresse.png", Dico)