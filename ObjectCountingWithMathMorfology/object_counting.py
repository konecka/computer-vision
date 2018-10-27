# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import morphology
from two_pass import two_pass_labeling

def count(labeled):
    return len(set(labeled.ravel()))

def find_objects(image):
    
    struct1 = np.array([[1, 1, 1],
                        [1, 1, 1], 
                        [1, 1, 1]])
    
    struct2 = np.array([[1, 1, 0, 0, 1, 1],
                        [1, 1, 0, 0, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1]])
    
    struct3 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 0, 0],
                        [1, 0, 0],
                        [1, 1, 1],
                        [1, 1, 1]])
    
    struct4 = np.array([[1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 0, 0, 1, 1],
                        [1, 1, 0, 0, 1, 1]])
    
    
    struct5 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [0, 0, 1],
                        [0, 0, 1],
                        [1, 1, 1],
                        [1, 1, 1]])
    

    res1 = two_pass_labeling(morphology.binary_erosion(image, struct1).astype("uint8"))
    res2 = two_pass_labeling(morphology.binary_erosion(image, struct2).astype("uint8"))
    res3 = two_pass_labeling(morphology.binary_erosion(image, struct3).astype("uint8"))
    res4 = two_pass_labeling(morphology.binary_erosion(image, struct4).astype("uint8"))
    res5 = two_pass_labeling(morphology.binary_erosion(image, struct5).astype("uint8"))


    return res1, res2, res3, res4, res5


if __name__== "__main__":
    image = np.load("./ps.npy.txt").astype("uint8")
    
    res1, res2, res3, res4, res5 = find_objects(image)
    
    sum_objects = 0
    
    no_holes = count(res1)
    sum_objects += no_holes
    
    hole_on_top = count(res2)
    sum_objects += hole_on_top
    
    hole_on_right = count(res3)
    sum_objects += hole_on_right
    
    hole_on_bottom = count(res4)
    sum_objects += hole_on_bottom
    
    hole_on_left = count(res5)
    sum_objects += hole_on_left
    
    print(no_holes) # 92
    print(hole_on_top) # 187
    print(hole_on_right) # 94
    print(hole_on_bottom) # 188
    print(hole_on_left) # 123
    print(sum_objects) # 684
    
#    plt.figure()
#    plt.subplot(121)
#    plt.imshow(image)
#    
#    plt.subplot(122)
#    plt.imshow(res1)
#    plt.show()

    
    