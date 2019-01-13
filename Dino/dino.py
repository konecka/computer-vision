# -*- coding: utf-8 -*-

import mss
import pyautogui
#import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import time
import cv2
from skimage.measure import label, regionprops
    

def image_prep(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, 
    cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # ночной режим, но в игре почему-то не включается
    if (np.mean(image) > 100):
        im_bw = cv2.bitwise_not(im_bw)

    return im_bw
    
    
    
if __name__ == "__main__":
#    webbrowser.open("http://www.trex-game.skipser.com/")
    webbrowser.open("https://chromedino.com/")
    time.sleep(4)
    pyautogui.press("up")
    
    time.sleep(2)
    with mss.mss() as sct:
         monitor = sct.monitors[1]
         image = np.array(sct.grab(monitor))
            
    
    bin_image = image_prep(image)
    cv2.imwrite("bin.jpg", bin_image)
    LB = label(bin_image)
    
    minr = minc = maxr = maxc = 0
    
    dino_template = cv2.imread("dino.jpg")
    dino_template = cv2.cvtColor(dino_template, cv2.COLOR_BGR2GRAY)
    dino_template = cv2.GaussianBlur(dino_template, (3, 3), 0)
    
    
    m = 100000
    for region in regionprops(LB):
        bbox = region.bbox
        img = bin_image[bbox[0]:bbox[2], bbox[1]:bbox[3]]
        img = cv2.resize(img, (dino_template.shape[1], dino_template.shape[0]))
        diff = cv2.absdiff(dino_template, img)
        
        if diff.sum() < m:
            minr, minc, maxr, maxc = bbox

#        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
#                                fill=False, edgecolor='red', linewidth=2)
        
    w = maxc - minc
    h = maxr - minr    
    
    disnance = maxc + int(3.2*w)
    start_time = time.time()
    game = True
    
    try:
        while game:     
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                
                image = np.array(sct.grab(monitor))
                bin_img = image_prep(image)
                
#                image = np.array(sct.grab(monitor))            
#                b_img = image_prep(image)

            if (bin_img[minr-int(h/6): minr-int(h/7), maxc:disnance] == 255).any():
                pyautogui.keyDown("down", pause=0.4)
                pyautogui.keyUp("down")
                time.sleep(0.2)
                
                    
            if (bin_img[minr+int(h/1.6): minr+int(h/1.5), maxc:disnance] == 255).any():
                    pyautogui.press("up")
   
            if (time.time() - start_time) >= 10:
                if disnance + int(w/2) <= bin_img.shape[1]:
                    disnance += int(w/4)
                    start_time = time.time()
                
#            if np.all(bin_img == b_img):
#                game = False
    
                    
    except KeyboardInterrupt:
        print("\n")

            