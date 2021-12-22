#!/usr/bin/python

from random import randint
from sys import argv
from panelgen.utils import *
from panelgen import panels

img = new_map(1000, 1000)
min_w = 0.05
max_w = 0.3
min_h = 0.05
max_h = 0.3

# Put square randomly on the image
img = panels.gen_panels(img, int(argv[1]), min_w, max_w, min_h, max_h, 1, 3)
print(img)


cv2.imwrite('out.png', img)
cv2.imshow("img", img)
cv2.waitKey(0)