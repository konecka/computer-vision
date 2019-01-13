# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt
import neighbors as nb
     
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
    
def is_slanted(y, x, two_neighbors, image):
    c = 0
    for pair in nb.corner_neighbors(y, x, image):
        if pair is not None:
            if image[pair[0]] == 0 and image[pair[1]] == 0:
                c += 1
            if not( pair[0] in two_neighbors) and not(pair[1] in two_neighbors):
                if (image[pair[0]] + image[pair[1]] > 1):
                    return 1
    if c == 4:
        return 1
        
    return 0

def get_two_neighbors(y, x, boundaries, image):
    two_neighbors = []
    neighbors_one = nb.d_neighbors(y, x, image)
    neighbors_two = nb.neighbors4(y, x, image)

    for n in neighbors_one:
            if n is not None:
                if(image[n] == 1 and n in get_boundaries(image)):
                    two_neighbors.append(n)
                    if len(two_neighbors) == 2:
                        break
    if len(two_neighbors) < 2:
        for n in neighbors_two:
            if n is not None:
                if(image[n] == 1 and n in get_boundaries(image)):
                    two_neighbors.append(n)
                    if len(two_neighbors) == 2:
                        break
    return two_neighbors
    
               
        
def perimeter(image, label=1, base_label=0):
    boundaries = get_boundaries(image, label)
    slanted = 0
    for (y, x) in boundaries:
        
        two_neighbors = get_two_neighbors(y, x, boundaries, image)

        if is_slanted(y, x, two_neighbors, image):
            slanted += 1
    print(slanted)      
    return len(boundaries) + slanted*math.sqrt(2) - slanted

    
if __name__ == "__main__":
    
    image = np.zeros((16, 16))
    
    LB = np.zeros((16, 16))
#    LB[4:, :4] = 1
    
#    LB[3:10, 8:] = 1
    
    LB[[3, 4, 3],[8, 8, 9]] = 1
    LB[[8, 9, 9],[8, 8, 9]] = 1
    LB[[3, 4, 3],[-2, -1, -1]] = 1
    LB[[9, 8, 9],[-2, -1, -1]] = 1
    
    LB[12:-1, 6:9] = 1
    
#    image[3, 4, 3],[8, 8, 9] = 1
#    image[1, 1:6] = 1
#    image[1, 4:6] = 1
#    image[2, 2:7] = 1
#    image[3, 3:5] = 1
#    image[4, 2:4] = 1
#    image[5, 3:4] = 1
    
#    image = np.zeros((20, 20))
#    image[5:9, 5:9] = 1
    
    
    print(perimeter(LB))
      
    plt.figure(1)
    plt.imshow(image)
    plt.show()
    