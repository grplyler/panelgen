import cv2
import numpy as np
import random
import cairo
import math
import yaml
from box import Box

def f2px(size, f):
    return size * f

def px2f(full_px, px):
    return px / full_px

def circle(w, h, depth):
    # data = np.zeros((h, w, 4))
    surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, w, h)
    c = cairo.Context(surface)
    c.scale(w, h)
    c.set_source_rgb(0.5, 0, 0)
    c.set_line_width(0.2)
    c.arc(0.5, 0.5, 0.25, 0, 2 * math.pi)
    c.fill()
    buf = surface.get_data()
    return np.ndarray(shape=(h, w), dtype=np.uint16, buffer=buf)


def radial_gradient(panel, size, low, high):
    x_axis = np.linspace(-1, 1, size)
    y_axis = np.linspace(-1, 1, size)

    xx, yy = np.meshgrid(x_axis, y_axis)
    arr = np.sqrt(xx**2 + yy**2)

    # Interpolate inner and outer colors
    inner = np.array([high, high, high])[None, None, :]
    outer = np.array([low, low, low])[None, None, :]

    arr /= arr.max()
    arr = arr[:, :, None]
    arr = arr * outer + (1 - arr) * inner

    # normalize to image
    # arr *= 255.0/arr.max()
    arr = arr.astype(np.uint8)
    # arr = np.stack((arr,)*3, axis=-1)

    return arr



def groove_constant(panel, inset, width, depth_change):
    p = panel
    dc = depth_change

    # Left Groove
    # create left goove inlay
    h = panel.shape[0] - (width * 2)
    d = panel[0, 0][0] + dc
    inlay = new_map(h, width, (d, d, d))
    x = width
    y = width
    panel = merge(panel, inlay, x, y)

    # Right groove
    h = panel.shape[0] - (width * 2)
    d = panel[0, 0][0] + dc
    inlay = new_map(h, width, (d, d, d))
    x = panel.shape[1] - (width * 2)
    y = width
    panel = merge(panel, inlay, x, y)

    # Top Groove
    h = width
    d = panel[0, 0][0] + dc
    w = panel.shape[1] - (width * 2)
    inlay = new_map(h, w, (d, d, d))
    print(inlay.shape)
    x = width
    y = width
    panel = merge(panel, inlay, x, y)

    # Bottom Groove
    h = width
    d = panel[0, 0][0] + dc
    w = panel.shape[1] - (width * 2)
    inlay = new_map(h, w, (d, d, d))
    print(inlay.shape)
    x = width
    y = panel.shape[0] - (width * 2)
    panel = merge(panel, inlay, x, y)

    return panel


def perc2px(wf, hf, w, h):
    return (int(w * wf), int(h * hf))


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


def new_map(width, height, color):
    img = np.zeros((width, height, 3), np.uint8)
    img[:] = color
    return img


def merge(bottom, top, x, y):
    th = top.shape[0]
    tw = top.shape[1]

    bottom[y:y + th, x:x + tw] = top[:]
    return bottom


def merge_add(bottom, top, x, y):
    th = top.shape[0]
    tw = top.shape[1]

    bottom[y:y + th, x:x + tw] = top[:]
    return bottom


def overlay(bottom, top, x, y):
    th = top.shape[0]
    tw = top.shape[1]

    # get pixels that will be overwritten
    under = bottom[y:y + th, x:x + tw]
    for i in range(under.shape[0]):
        for j in range(under.shape[1]):

            # if the pixel in the top is brighter, set the
            # value under from the top
            if top[i][j][0] > under[i][j][0]:
                under[i][j] = under[i][j] * (top[i][j] / 20)

    bottom[y:y + th, x:x + tw] = under[:]
    return bottom
