# -*- coding: utf-8 -*-

import numpy as np
from scipy.ndimage import morphology
import matplotlib.pyplot as plt


def convolve(image, mask):
    bordered = np.zeros((image.shape[0] + 2, image.shape[1] + 2), dtype="f4") 
    bordered[1:-1, 1:-1] = image
    
    convolved = np.zeros_like(bordered)
    
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 1:
                convolved[y,x]=(mask*bordered[y:y+3,x:x+3]).sum()     
    return convolved 
            
def perimeter(image, lb):
#    print(image)
    LB = np.zeros((image.shape[0], image.shape[1]))
    LB = LB.astype(np.uint8)
    coords = np.where(image == lb)
    
    for y, x in zip(coords[0], coords[1]):
        LB[y, x] = 1
    
    eroded_image = morphology.binary_erosion(LB)
    
    border_image = LB - eroded_image
#    print(border_image)
    mask = np.array([[10, 2, 10], 
                     [2, 1, 2], 
                     [10, 2, 10]])
    

    perimeter_image = convolve(border_image, mask)
    perimeter_image = perimeter_image.astype(np.uint8)
    
#    print(perimeter_image)
    
    perimeter_weights = np.zeros(50, dtype=np.double)
    perimeter_weights[[5, 7, 15, 17, 25, 27]] = 1
    perimeter_weights[[21, 33,43,  47]] = np.sqrt(2)
    perimeter_weights[[13, 23, 35]] = (1 + np.sqrt(2)) / 2
    

    p = perimeter_weights[perimeter_image].sum()
    
    return p

            
    


if __name__ == "__main__":
    
    mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    
    LB = np.zeros((16, 16))
#    
    LB[4:, :4] = 2
    
    LB[3:10, 8:] = 1
    LB[[3, 4, 3],[8, 8, 9]] = 0
    LB[[8, 9, 9],[8, 8, 9]] = 0
    LB[[3, 4, 3],[-2, -1, -1]] = 0
    LB[[9, 8, 9],[-2, -1, -1]] = 0
    
    LB[12:-1, 6:9] = 3
    
    LB[11:15, 10:16] = 4
    LB[13:15, 13] = 0
    
    print("Object 1 =", perimeter(LB, 1))
    print("Object 2 =", perimeter(LB, 2))
    print("Object 3 =", perimeter(LB, 3))
    print("Object 4 =", perimeter(LB, 4))
    
#    print("Object 1 =", perimeter(LB, 1))
    
    plt.figure()
    plt.imshow(LB)
    plt.show()
    

    
