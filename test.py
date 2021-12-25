#!/usr/bin/python
import cairo
import cv2
import random
from PIL import Image, ImageChops
size = 1024
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, size,
                                          size)
c = cairo.Context(surface)
# c.scale(size, size)

def wrap_rect(c, x, y, w, h, rgb):

    # setup pen
    c.set_source_rgb(*rgb)

    # draw first rect
    c.rectangle(x, y, w, h)

    # calulate right side overlap
    x_over = 1.0 - (x + w)
    y_over = 1.0 - (y + h)
    x_wrap = abs(x_over)
    y_wrap = abs(y_over)

    # If over are negative, we need to wrap the image
    if x_over < 0.0:
        # wrap x wrap
        c.rectangle(0.0, y, x_wrap, h)

    if y_over < 0.0:
        y_wrap = abs(y_over)
        c.rectangle(x, 0.0, w, y_wrap)

    # if x and y are over:
    if x_over < 0.0 and y_over < 0.0:
        print('xy wrap')
        c.rectangle(0.0, 0.0, x_wrap, y_wrap)


    print("x_over:", x_over)
    print("y_over", y_over)

    c.fill()

def wrap_texture(base, tex, x, y):
    x = round(base.width * x)
    y = round(base.height * y)

    # randomize height
    rand_h = round(255 * random.uniform(0.2, 1.0))
    mult = Image.new('RGBA', tex.size, (rand_h, rand_h, rand_h))
    
    tex = ImageChops.multiply(tex, mult)
    

    # find x overlap
    x_over = base.width - (x + tex.width)
    y_over = base.height - (y + tex.height)

    if x_over < 0:
        left = tex.width - abs(x_over)
        top = 0
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (0, y), crop)

    if y_over < 0:
        left = 0
        top = tex.height - abs(y_over)
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (x, 0), crop)

    if y_over < 0 and x_over < 0:
        left = tex.width - abs(x_over)
        top = tex.height - abs(y_over)
        right = tex.width
        bottom = tex.height
        crop = tex.crop((left, top, right, bottom))
        base.paste(crop, (0, 0), crop)

    print("x over:", x_over)
    print("y over:", y_over)

    base.paste(tex, (x, y), tex)

# load texture
base = Image.new('RGBA', (1024, 1024))
tex = Image.open('slab.png')


for i in range(16):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    wrap_texture(base, tex, x, y)

base.save('out.png')