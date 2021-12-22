import cv2
import numpy as np
import random

def perc2px(wf, hf, w, h):
    return (int(w*wf), int(h*hf))

def randfitpos(fit_w=100, fit_h=100, max_x=1024, max_y=1024):
    # return ran*dom position in image
    x = random.random()
    y = random.random()
    
    # Generate Random positions until they fit
    while True:
        x = int(random.random() * max_x)
        y = int(random.random() * max_y)
        if (x + fit_w <= max_x) and (y + fit_h <= max_y):
            return x, y
        else:
            print('warn: generated pos out of bounds')


def new_map(width, height):
    img = np.zeros((width, height, 3), np.uint8)
    return img

def merge(bottom, top, x, y):
    bh = bottom.shape[0]
    bw = bottom.shape[1]
    th = top.shape[0]
    tw = top.shape[1]

    bottom[y:y+th, x:x+tw] = top[:]
    return bottom
