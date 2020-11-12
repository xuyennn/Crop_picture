from PIL import Image
import os
import cv2
def prep(Path):
    im = cv2.imread("/home/mcrpc/Downloads/Ảnh drone/"+Path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # W = 250
    # height, width, depth = im.shape
    # scale = W/width
    # newX, newY = im.shape[1]*scale, im.shape[0]*scale
    # res = cv2.resize(im, (int(newX),int(newY)))
    # if not os.path.exists("/home/kinginthenet/Documents/Ảnh drone/temp/"+Path.split(".")[0]+"/"):
    #         os.mkdir("/home/kinginthenet/Documents/Ảnh drone/temp/"+Path.split(".")[0]+"/")
    # cv2.imwrite("/home/kinginthenet/Documents/Ảnh drone/temp/" + Path.split(".")[0]+".jpg", res)
    M = im.shape[0]//8
    N = im.shape[1]//8
    tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
    x = 1
    y = 1
    for tile in tiles:
        if x > 8:
            y+=1
            x=1
#duong dan de luu file moi
        file = "/home/mcrpc/Downloads/OpenLabeling/main/input/"+Path.split(".")[0]+"_"+str(y)+"_"+str(x)+".jpg"
        cv2.imwrite(file, tile)
        x+=1
        
        

#crop("20190924_095719.jpg")
list = os.listdir("/home/mcrpc/Downloads/Ảnh drone/")
for img in list:
    print(img)
    if img.split(".")[0]=="temp":
        continue
    else:
        prep(img)
    
#crop("/home/kinginthenet/Documents/","hina.jpg",1080,1920, 0, )
# im = cv2.imread("drone.jpg")
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
# M = im.shape[0]//8
# N = im.shape[1]//8
# tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
# name = 0
# for tile in tiles:
#     file = str(name)+".jpg"
#     cv2.imwrite(file, tile)
#     name+=1
# print(type(im))
