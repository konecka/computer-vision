# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def draw_circle(X, Y, R, image):
    x = error = 0
    y = R
    delta = 1 - 2 * R
    while(y >= 0):
        image[Y+y, X+x] = 1
        image[Y-y, X+x] = 1
        image[Y+y, X-x] = 1
        image[Y-y, X-x] = 1
        
        error = 2 * (delta +y)-1
        
        if (delta < 0) and (error <= 0):
            x +=1
            delta += 2 * x + 1
            continue
        if (delta > 0) and (error > 0):
            y -= 1
            delta -= 2 * y + 1
            continue
        x += 1
        delta += 2 * (x-y)
        y -=1

        
if __name__ == "__main__":
    r = 150
    image = np.zeros((int(2*r+r/2), int(2*r+r/2)))
    draw_circle(int(image.shape[1]/2), int(image.shape[0]/2), r, image)
    plt.figure()
    plt.imshow(image)
    plt.show()
    
    

