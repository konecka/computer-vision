# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

def check(sub, masks):
    for mask in masks:
        if np.all(sub==mask):
            return True
    return False

def count_objects(image, outer_mask, inter_mask):
    outer = inner = 0
    for y in range(1, image.shape[0]-1):
        for x in range(1, image.shape[1]-1):
#            if image[y, x] == 1:
            sub = image[y-1:y+1, x-1:x+1]
            if check(sub, outer_mask):
                    outer+=1
            if check(sub, inter_mask):
                    inner += 1
    return (outer-inner)/4
    
    
if __name__ == "__main__":
    outer_mask = [np.array([[0, 0], [0, 1]]), np.array([[0, 0], [1, 0]]),
                  np.array([[1, 0], [0, 0]]), np.array([[0, 1], [0, 0]])]
    inter_mask = [np.array([[0, 1], [1, 1]]), np.array([[1, 0], [1, 1]]),
                  np.array([[1, 1], [0, 1]]), np.array([[1, 1], [1, 0]])]
    
    path = './objects/'
#    print(os.listdir(path))
    for f in os.listdir(path):
        img = np.load(os.path.join(path, f))
        num_objects = count_objects(img, outer_mask, inter_mask)
        print(num_objects)
#        plt.imshow(img)


