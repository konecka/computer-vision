# -*- coding: utf-8 -*-

def check(image, y, x):
    if not 0 <= x < image.shape[0]:
        return False
    if not 0 <= y < image.shape[1]:
        return False
    return True

def d_neighbors(y, x, image):
    lt = (y-1, x-1)
    rt = (y-1, x+1)
    rb = (y+1, x+1)
    lb = (y+1, x-1)
    
    if not check(image, *lt):
        lt = None

    if not check(image, *rt):
        rt = None
        
    if not check(image, *rb):
        rb = None

        
    if not check(image, *lb):
        lb = None

    
    return lt, rt, rb, lb
    

def neighbors4(y, x, image):
    t = (y-1, x)
    r = (y, x+1)
    b = (y+1, x)
    l = (y, x-1)
    
    if not check(image, *t):
        t = None
    if not check(image, *r):
        r = None
    if not check(image, *b):
        b = None
    if not check(image, *l):
        l = None
    
    return t, r, b, l

def corner_neighbors(y, x, image):
    pair1 = ((y-1, x), (y, x+1))
    pair2 = ((y, x+1), (y+1, x))
    pair4 = ((y, x-1), (y-1, x))
    pair3 = ((y+1, x), (y, x-1))
    
    if not check(image, *pair1[0]) or not check(image, *pair1[1]):
        pair1 = None
    if not check(image, *pair2[0]) or not check(image, *pair2[1]):
        pair2 = None
    
    if not check(image, *pair3[0]) or not check(image, *pair3[1]):
        pair3 = None
    if not check(image, *pair4[0]) or not check(image, *pair4[1]):
        pair4 = None
    
    return pair1, pair2, pair3, pair4

def neighbors8(y, x, image):    
    lt = image[y-1, x-1] if check(image, y-1, x-1) else 0
    t = image[y-1, x] if check(image, y-1, x) else 0
    rt = image[y -1, x+1] if check(image, y -1, x+1) else 0
    
    l = image[y, x-1] if check(image, y, x-1) else 0
    c = image[y, x]
    r = image[y, x+1] if check(image, y, x+1) else 0
    
    lb = image[y + 1, x-1] if check(image, y + 1, x-1) else 0
    b = image[y+1, x] if check(image, y+1, x) else 0
    rb = image[y+1, x+1] if check(image, y+1, x+1) else 0
    
    block = [[lt, t, rt], [l, c, r], [lb, b, rb]]
    
    return block

