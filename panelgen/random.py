import random

from numpy.random.mtrand import rand
from panelgen.panels import Spec
from panelgen.config import g

def float_range(min, max):
    return random.uniform(min, max)

def randomize(cnf):
    for key, value in cnf.randomize.items():
        r = None
        if value['kind'] == 'float_range':
            r = float_range(value['min'], value['max'])
            cnf.rand[key] = r

    return cnf
