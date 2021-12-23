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
gen.cnf.base.w = int(argv[1])
gen.cnf.base.h = int(argv[1])
gen.cnf.panel.count = int(argv[2])
gen.generate()
# print(gen.conf)
exit(1)

spec = panels.Spec(fill_rgb=(0.0, 1, 0.0),
                   fill=True,
                   stroke=True,
                   stroke_px=5,
                   groove=True,
                   groove_px=10,
                   groove_inset_px=10,
                   rivets=True,
                   rivet_inset_px=26)
rnd = Randomizer(x=True,
                 y=True,
                 w=True,
                 h=True,
                 fill=True,
                 stroke=True,
                 spec=spec,
                 min_h=min_h,
                 min_w=min_h,
                 max_h=max_h,
                 max_w=max_w)

# Put square randomly on the image
# img = panels.gen_panels(img, int(argv[3]), min_w, max_w, min_h, max_h, 1, 3)
panel = panels.Panel(int(argv[1]), int(argv[1]), (0, 0, 0))
# panel.circle(rgb_fill=(1,1,1))
for i in range(int(argv[2])):
    panel.rect(rnd=rnd)
    # panel.roundrect(rnd=rnd)
    rnd.run()

panel.save()
panel.display('out.png')
cv2.destroyAllWindows()
# print(img)

# cv2.imwrite('out.png', img)
# cv2.imshow("img", img)
# cv2.waitKey(0)