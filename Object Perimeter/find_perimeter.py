# -*- coding: utf-8 -*-

import math
import numpy as np
import neighbors as nb
from skimage import morphology
import matplotlib.pyplot as plt

def get_boundaries(LB, label=1):
    pos = np.where(LB == label)
    boundaries = []
    for y, x in zip(*pos):
        
        for n in(nb.neighbors4(y, x, image)):
            if n is not None:
                yn = n[0]
                xn = n[1]
                if yn < 0 or yn > LB.shape[0] -1:
                    boundaries.append((y, x))
                    break
                elif xn < 0 or xn > LB.shape[1] -1:
                    boundaries.append((y, x))
                    break
                elif LB[yn, xn] != label:
                    boundaries.append((y, x))
                    break
    return boundaries



def convolve(mask, image):
    boundaries = get_boundaries(image)
    convolved = []

    for y, x in boundaries:
        print('y-x ', y, x)
        block = nb.neighbors8(y, x, image)
        print(block)
        accum = np.sum(mask*block)
        print('accum ', accum)
        convolved.append(accum)
    
    print(convolved)
    return convolved
            
def perimeter(image, label=1):
    boundaries = get_boundaries(image, label)
    
    contour = np.zeros((image.shape[0], image.shape[1]))
    
    for p in boundaries:
        contour[p[0], p[1]] = 1
    
    mask = np.array([[10, 2, 10], [2, 1, 2], [10, 2, 10]])
    
    convolve(mask, image)
    
    return(contour)

#    

    


if __name__ == "__main__":
    
    image = np.zeros((7, 7))

#    image[0, 5] = 1
#    image[1, 1:6] = 1
#    image[1, 4:6] = 1
#    image[2, 2:7] = 1
#    image[3, 3:5] = 1
#    image[4, 2:4] = 1
#    image[5, 3:4] = 1
    
    
    image = np.zeros((9, 9))
    image[1, 1:8] = 1
    image[2, 1:8] = 1
    image[3, 1:4] = 1
    image[4, 1:8] = 1
    image[5, 1:8] = 1
    
    c = perimeter(image)
#    
    plt.figure(1)
    plt.imshow(image)

    plt.show()