

from numpy import square
from panelgen.utils import *
import numpy as np
import random

def square(size=100, depth=255, border=10):
    img = new_map(size, size)
    img[:] = (depth, depth, depth)
    return img

def rect(w=100, h=100, depth=255, border=10):
    img = np.zeros((h,w,3), np.uint8)
    img[:] = (depth, depth, depth)
    return img


def gen_panels(base, n_panels, min_w, max_w, min_h, max_h, rc=0, rm=1):
    
    print("base w:", base.shape[1])
    print("base h:", base.shape[0])

    for i in range(n_panels):
        # Make random size panel
        wf = random.uniform(min_w, max_w)
        hf = random.uniform(min_h, max_h)
        depth = random.randint(0, 255)

        # convert w and f
        w, h = perc2px(wf, hf, base.shape[1], base.shape[0])
        print("w:", wf, w)
        print("h:", hf, h)
        panel = rect(w, h, depth, 10)

        x, y = randfitpos(w, h, base.shape[1], base.shape[0])
        print(x, y)
        base = merge(base, panel, x, y)

    # TODO: find a way to make this recursive
    # we're done
    return base
