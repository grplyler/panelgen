import random

from numpy.random.mtrand import rand
from panelgen.panels import Spec


class Randomizer(object):
    def __init__(self,
                 x=False,
                 y=False,
                 w=False,
                 h=False,
                 spec=None,
                 min_x=0.0,
                 max_x=1.0,
                 min_y=0.0,
                 max_y=1.0,
                 min_w=0.04,
                 max_w=0.5,
                 min_h=0.04,
                 max_h=0.5,
                 fit=False,
                 fill=False,
                 stroke=False) -> None:
        super().__init__()
        self.fit = fit
        self.rx = x
        self.ry = y
        self.rw = w
        self.rh = h
        self.rfill = fill
        self.rstroke = stroke
        self.rdepth = True
        self.spec = spec

        if spec is None:
            self.spec = Spec()

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_h = min_h
        self.max_h = max_h
        self.min_w = min_w
        self.max_w = max_w

        self.x = 0.0
        self.y = 0.0
        self.w = 0.0
        self.h = 0.0

        self.run()

    def random_fit(self, a):
        while True:
            r = random.uniform(0.0, 1.0)

            # See if we fit
            if r + a < 1.0:
                return r
            else:
                print('out of bounds')

    def run(self):

        if self.rh:
            self.h = random.uniform(self.min_h, self.max_h)
            self.spec.h = self.h
        if self.rw:
            self.w = random.uniform(self.min_w, self.max_w)
            self.spec.w = self.w
        if self.rdepth:
            r = random.uniform(0.0, 0.7)
            self.spec.stroke_rgb = (r, r, r)

        # Randomize locations until they inside
        if self.rx:
            self.x = self.random_fit(self.w)
            self.spec.x = self.x
        if self.ry:
            self.y = self.random_fit(self.h)
            self.spec.y = self.y

        # Randomize Color
        if self.rfill:
            r = random.uniform(0.0, 1.0)
            self.spec.fill_rgb = (r, r, r)
        if self.rstroke:
            r = random.uniform(0.0, 1.0)
            self.spec.stroke_rgb = (r, r, r)
