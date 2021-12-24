#!/usr/bin/python

from random import randint
from sys import argv
from panelgen.utils import *
from panelgen import panels
from panelgen.random import Randomizer
from panelgen.generator import Generator

# img = new_map(int(argv[1]), int(argv[2]), (0, 0, 0))
min_w = 0.02
max_w = 0.3
min_h = 0.02
max_h = 0.3

gen = Generator()

# Pull some configuration from command line
gen.cnf.base.type = argv[1]
print("creating", argv[1], "type panels")
gen.cnf.base.w = int(argv[2])
gen.cnf.base.h = int(argv[2])
gen.cnf.types[argv[1]].count = int(argv[3])
gen.generate('panel')
