# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.ndimage import map_coordinates
import cv2
import os


def stereographic_proj(phi, theta):
    
    R=np.sin(phi)/(1-np.cos(phi)+0.000000001)
    Th=theta
    R=(R-1)/np.max(R)
    
    return R, Th
    
    
def orthographic_proj(phi, theta):
    
    R=np.cos(phi)
    Th=theta    
    R=R/np.max(R)
    
    return R, Th  
    
    
def polar2cartesian(r, t, grid, x, y, order=0):

    X, Y = np.meshgrid(x, y)

    new_r = np.sqrt(X*X+Y*Y)
    new_t = np.arctan2(Y,X)

    ir = interp1d(r, np.arange(len(r)), bounds_error=False)
    it = interp1d(t, np.arange(len(t)))

    new_ir = ir(new_r.ravel())
    new_it = it(new_t.ravel())

    return map_coordinates(grid, np.array([new_ir, new_it]),
                            order=order).reshape(new_r.shape)


if __name__ == "__main__":
        
    segment=cv2.cvtColor(cv2.imread('Segment.bmp'), cv2.COLOR_BGR2GRAY)

    
     
    #For number of clusters in the segmented image
    for i in range(34):
        
        band=np.zeros([70, 180])    
        index=0
        segment_index=i
        for out in range(180):
            
            for index in range(70):
                index2=index+out*70
                band[index, out]=np.average(np.extract(segment==segment_index, storage[:,:,index2]))
        
        nr = 70
        nt = 180
        
        
        
        phi = np.linspace(np.pi/2,np.pi/2 - 34.5*(np.pi/180), 70)
    
        th = np.linspace(-np.pi, np.pi, nt)
        z = band
        
        # Define new cartesian grid
        
        nx = 256
        ny = 256
        
        x = np.linspace(-1., 1., nx)
        y = np.linspace(-1., 1., ny)
        
        
        r_p, th_p=stereographic_proj(phi, th)
        #r_p, th_p=orthographic_proj(phi, th)
        
        
        band_out=polar2cartesian(r_p, th_p, z, x, y, order=3)
        band_out[np.where(band_out==0)]=np.mean(z)
        
        fig = plt.figure()
        plt.title('Segment Index = %i' %segment_index)
        
        ax = fig.add_subplot(121)
        fig.subplots_adjust(left=0.25, bottom=0.25)    
        im1=ax.imshow(band_out, interpolation='nearest', cmap='Greys_r')
        ax.axis('off')
        
        ax2 = fig.add_subplot(122)  
        im2=ax2.imshow(segment==segment_index, cmap='Greys_r')
        ax2.axis('off')
        
        filename = os.getcwd() +'/Band/'+str(i)+'band.png'
        fig.savefig(filename, bbox_inches='none') 
        plt.close(fig)
        
        filename = os.getcwd()+'/Band/'+str(i)+'band.npy'  
        np.save(filename, band_out)
