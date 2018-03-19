# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
from utils import Stitcher

if __name__ == "__main__":
    imageB=cv2.imread("1.bmp")
    stitcher = Stitcher()
    storage=np.zeros([442,512,12600])
    storage[:,:,0]=cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)
    for i in range(12600):
    
        fileref=str(i+2)+".bmp"    
        imageA=cv2.imread(fileref)
     
        result = stitcher.stitch([imageA, imageB], showMatches=True)
        storage[:,:,i+1]=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)



    os.chdir(os.getcwd() +'\\AlignedSIFT')
    np.save("Aligned.npy", storage)
    for i in range(14040):
        im=storage[:,:,i]
        cv2.imwrite(str(i)+'.bmp',im)
    





