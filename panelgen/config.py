from box import Box
import operator as op
import yaml
from box import Box
from flatten_dict import flatten

def g(box, item):
    return op.attrgetter(item)(box)

def dot_reducer(k1, k2):
    if k1 is None:
       return k2
    else:
        return k1 + "." + k2

def make_flat(d):
    return flatten(d, reducer=dot_reducer)

def load_config(fname):
    with open(fname) as f:
        y = yaml.safe_load(f)
        box = Box(y)
        box.flat = flatten(y, reducer=dot_reducer)
        return box