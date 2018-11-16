# -*- coding: utf-8 -*-

import os
import numpy as np

def load(path):
    size = 0
    image = []
    with open(path) as file:
        for i, row in enumerate(file):
            if i == 0:
                size = float(row)
            elif i == 1:
                continue
            else:
                image.append(list(map(int,row.split())))
    return size, np.array(image)

def neighbors(y, x):
    return ((y, x+1), (y+1, x), (y, x-1), (y-1, x))

def get_boundaries(LB, label=1):
    pos = np.where(LB == label)
    boundaries = []
    i = 0
    for y, x in zip(*pos):
        n = neighbors(y, x)
        for i in range(len(n)):
            ny, nx = n[i]
            if LB[n[i][0]-1, n[i][1]-1] == label:
                i+=1
        if i!=4:
            boundaries.append((y, x))
    return boundaries        
            
def distance(px1, px2):
    return ((px1[0] - px2[0])** 2 +
            (px1[1] - px2[1])** 2) ** 0.5
            
def nominal_resolution(image, r_size):
    boundaries = get_boundaries(image)
    distances = []
    
    for p1 in boundaries:
        for p2 in boundaries[1:-1]:
            distances.append(distance(p1, p2))
    if not distances:
        return 0
    else:
        return  max(distances) /r_size

if __name__ == "__main__":
    
    path = "figures"
    for file in os.listdir(path):
        r_size, img = load(os.path.join(path, file))
        print(file, ' - ', nominal_resolution(img, r_size))

    


