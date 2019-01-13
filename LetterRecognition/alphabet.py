# -*- coding: utf-8 -*-
import numpy as np
from skimage import filters
from skimage.measure import label, regionprops
from skimage import morphology
from skimage import draw
import matplotlib.pyplot as plt
import collections



def count_holes(s):
    s = np.logical_not(s).astype('uint8')
    
    ss = np.ones((s.shape[0] + 2, s.shape[1] + 2))
    ss[1:-1, 1:-1] = s
    
    LBs = label(ss)
    LBs[LBs == 1] = 0
    
    return len(np.unique(LBs))-1

def count_hatch(s):
    up = s[0, :]
    upe = np.zeros(len(up) + 2)
    upe[1: -1] = up
    upe = np.abs(np.diff(upe))
    
    intervals = np.where(upe > 0)[0]
    points_up = []
    
    for p1, p2 in zip( intervals[::2], intervals[1::2]):
        points_up.append((p2+p1) // 2)
#    print(points_up)
    
    down = s[-1, :]
    downe = np.zeros(len(down) + 2)
    downe[1: -1] = down
    downe = np.abs(np.diff(downe))
    
    intervals = np.where(downe > 0)[0]
    points_down = []
    
    for p1, p2 in zip( intervals[::2], intervals[1::2]):
        points_down.append((p2+p1) // 2)    
    h = 0
    for p1 in points_up:
        for p2 in points_down:
            line = draw.line(0, p1, s.shape[0]-1, p2)

            if np.all(s[line] == 1):
                h += 1
    if h ==0:
        h = has_vline(s)
    return h

def has_vline(s):
    line = np.sum(s, 0) // s.shape[0]
    return 1 in line

def symb_center(s):
    s = np.logical_not(s).astype('uint8')
    
    ss = np.ones((s.shape[0] + 2, s.shape[1] + 2))
    ss[1:-1, 1:-1] = s
    
    LBs = label(ss)
    LBs[LBs == 1] = 0
    
#    labels = np.unique(LBs)
#    print(labels)
    
    coords_x = np.where(LBs == 2)[0]
    coords_y = np.where(LBs == 2)[1]
#    print(coords_y)
#    x_c = (max(coords_x) - min(coords_x))/2
#    y_c = (max(coords_y) - min(coords_y))/2
    x_c = np.mean(coords_x)
    y_c = np.mean(coords_y)
    
    return (y_c, x_c)

def recognite(s):
    holes = count_holes(s)
    if holes  == 2:
        hatches = count_hatch(s)
        if hatches == 1:
            return 'B'
        else:
            return '8'
    elif holes == 1:
        hatches = count_hatch(s)
        if hatches > 0:
            if has_vline(s):
                if symb_center(s)[1] <= s.shape[0]/2:
                    return 'P'
                else:
                    return 'D'
            else:
                return 'A'
        else:
            return '0'
        
    else:
        hatches = count_hatch(s)
        ratio = s.shape[0] / s.shape[1]
        
        if hatches == 4:
            return 'W'
        elif hatches == 2:
            return 'X'
        
        elif  ratio < 0.5:
            return '-'
        
        elif has_vline(s) and ratio > 1:
            return '1'
        
        elif hatches == 1 and 0.9 < ratio < 1.1:
            return '*'
        elif hatches == 1 and 1.9 < ratio < 2.1:
            return '/'
    return None
        
    

if __name__ == "__main__":
    alphabet = plt.imread("./images/symbols.png")
    
    alphabet = np.mean(alphabet, 2)
    
    thresh = filters.threshold_otsu(alphabet)
    
    alphabet[alphabet < thresh] = 0
    alphabet[alphabet >= thresh] = 1
    
    b_alpha = np.zeros_like(alphabet)
    b_alpha[alphabet < thresh] = 1
    b_alpha[alphabet >= thresh] = 0
    
    LB = label(alphabet)
    props = regionprops(LB)
    
#    s = props[7].image
#    print(len(props))

    defdict = collections.defaultdict()
    alph = {'strange_symbol':0}

    for i in range(len(props)):
        s = props[i].image
        symb = recognite(s)
        
        if symb == None:
            alph['strange_symbol'] += 1
        else:
            if symb in alph:
                alph[symb] += 1
            else:
                alph[symb] = 1

    count = 0
    
    for key in alph:
        if key !=  'strange_symbol':
            count += alph[key]
    print('Процент распознавания:', (count / len(props)  * 100))
    print(alph)

#    plt.imshow(s, cmap = 'gray')
#    plt.subplot(122)
##    plt.plot(upe)
##    plt.plot(downe)
#    plt.show()
    
