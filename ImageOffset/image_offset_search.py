# -*- coding: utf-8 -*-

import numpy as np


def find_offset(img1, img2):
    y1 = x1 = 0
    y2 = x2 = 0
    stat = 0
    for y in range(img1.shape[0]):
        for x in range(img1.shape[1]):
            if stat == -1:
                break
            elif stat == 0:
                if(img1[y, x] == 1):
                    y1 = y
                    x1 = x
                    stat = 1
                elif img2[y, x] == 1:
                    y2 = y
                    x2 = x
                    stat = 2
            elif stat == 1:
                if img2[y, x] == 1:
                    y2 = y
                    x2 = x
                    stat = -1
            elif stat == 2:
                if img1[y, x] == 1:
                    y1 = y
                    x1 = x
                    print(y, x)
                    stat = -1
    return (y1-y2, x1-x2)

if __name__ == "__main__":
    img1 = np.loadtxt("./img/img1.txt")
    img2 = np.loadtxt("./img/img2.txt")
    offsets = find_offset(img1, img2)
    print("X offset: " + str(offsets[1]))
    print("Y offset: " + str(offsets[0]))