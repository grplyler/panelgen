from math import pi
from numpy import square
from numpy.core.fromnumeric import reshape
from panelgen.utils import *
import numpy as np
import random
import cairo
import copy
from math import pi


class Spec(object):
    def __init__(self,
                 x=0.0,
                 y=0.0,
                 w=0.5,
                 h=0.5,
                 fill_rgb=(0.5, 0.5, 0.5),
                 stroke_rgb=(0.5, 0.5, 0.5),
                 fill=False,
                 stroke=True,
                 stroke_px=5,
                 groove=False,
                 groove_px=5,
                 groove_inset_px=10,
                 rivets=True,
                 rivet_inset_px=20) -> None:
        super().__init__()
        self.fill = fill
        self.stroke_px = stroke_px
        self.stroke = stroke
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fill_rgb = fill_rgb
        self.stroke_rgb = stroke_rgb
        self.groove = groove
        self.groove_px = groove_px
        self.groove_inset_px = groove_inset_px
        self.rivets = rivets
        self.rivet_inset_px = rivet_inset_px


class Panel(object):
    def __init__(self, cnf):
        self.cnf = cnf
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, cnf.base.w,
                                          cnf.base.h)
        self.c = cairo.Context(self.surface)
        self.c.scale(cnf.base.w, cnf.base.h)
        self.w = cnf.base.w
        self.h = cnf.base.h

    def save(self, fname='out.png'):
        self.surface.write_to_png(fname)

    def display(self, fname):
        img = cv2.imread(fname)
        cv2.imshow("img", img)
        cv2.waitKey(0)

    def circle(self,
               cx=0.5,
               cy=0.5,
               radius=0.25,
               line_width=0.01,
               rgb_fill=(0.5, 0.0, 0.0)):
        c = self.c

        c.set_source_rgb(rgb_fill[0], rgb_fill[1], rgb_fill[2])
        c.set_line_width(line_width)
        c.arc(cx, cy, 0.25, 0, 2 * math.pi)
        # c.stroke()
        c.fill()

    def rect(self, cnf):

        # context
        c = self.c

        c.set_line_width(px2f(self.w, cnf.border.thickness))
        c.set_line_cap(cairo.LINE_CAP_ROUND)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        c.set_fill_rule(cairo.FILL_RULE_WINDING)
        c.rectangle(cnf.flat['panel.x'], cnf.flat['panel.y'],
                    cnf.flat['panel.w'], cnf.flat['panel.h'])
        if cnf.panel.fill:
            elevation = cnf.flat['panel.elevation']
            c.set_source_rgb(elevation, elevation, elevation)
            c.fill()

    def angled(self, cnf):
        c = self.c

        # Configure stroke
        col = random.uniform(0.0, 1.0)
        c.set_source_rgb(1, 1, 1)
        c.set_line_width(px2f(self.w, 30))
        c.set_line_cap(cairo.LINE_CAP_ROUND)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        
        # Pick and edge
        choice = random.choice(['left', 'top', 'right', 'bottom'])

        # c.move_to(0, 0)
        # c.close_path()
        # if choice == 'left':
            # choose random x value
        y = random.uniform(0.0, 1.0)

        # choose random distance
        distance = random.uniform(0.0, 1.0)

        x = 0.0

        # draw line from left side to distnace
        print(x, y)
        c.move_to(x, y)
        c.line_to(distance, y)

        # Draw arc at 45 degree to to the end of the map
        arc_dist = random.uniform(0.05, 0.4)
        c.arc(distance, y, arc_dist, 7*pi/4, 7*pi/4)

        # draw straight line
        c.rel_line_to(1.0, 0.0)
        # c.close_path()

        c.stroke()

        print("picked:", choice)

    def rivets(self, spec):
        c = self.c
        inset_px = spec.rivet_inset_px
        inset_f = px2f(1024, inset_px)
        spacing = 20
        spacing_f = px2f(1024, spacing)
        print("under color:", spec.stroke_rgb[0])
        elevation = spec.fill_rgb[0] + 0.05
        print("elevation color:", elevation)
        dia = 10

        # setup stroke
        spec.stroke_rgb = (elevation, elevation, elevation)
        spec.fill_rgb = (elevation, elevation, elevation)
        c.set_source_rgb(*spec.stroke_rgb)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        c.set_line_cap(cairo.LINE_CAP_ROUND)
        c.set_line_width(px2f(self.w, 10))

        # Go to corner of the panel
        # c.move_to(spec.x + inset_f, spec.y + inset_f)
        print("spec.w", spec.w)
        offset = 0.0
        y = spec.y + inset_f
        x = spec.x + inset_f

        # Draw top and bottom rivets
        while x < (spec.x + spec.w - inset_f):
            # print("drawing rivet")
            c.move_to(x, y)
            c.close_path()
            c.move_to(x, spec.y + spec.h - inset_f)
            c.close_path()
            c.move_to(x, y)

            x = x + spacing_f
            print('x, y', x, y)
            print('spec.w', spec.w)
            print("spacing:", spacing_f)

        c.stroke()

        # Draw side rivets
        # move to starting point
        x = spec.x + inset_f
        y = spec.y + inset_f + spacing_f
        while y < (spec.y + spec.h - inset_f):
            c.move_to(x, y)
            c.close_path()
            c.move_to(spec.x + spec.w - inset_f, y)
            c.close_path()
            c.move_to(x, y)

            y = y + spacing_f
        c.stroke()

    def border(self, cnf):
        c = self.c
        inset = cnf.border.inset
        inset_f = px2f(self.cnf.base.w, inset)
        x = cnf.flat['panel.x']
        y = cnf.flat['panel.y']
        w = cnf.flat['panel.w']
        h = cnf.flat['panel.h']

        x = x + inset_f
        y = y + inset_f
        h = h - (inset_f * 2)
        w = w - (inset_f * 2)

        # Darken stroke to 80%
        p_elev = cnf.flat['panel.elevation']
        elev_change = cnf.border.elevation
        elev = p_elev + elev_change
        color = (elev, elev, elev)

        thickness = px2f(cnf.base.w, cnf.border.thickness)
        # setup stroke
        c.set_source_rgb(*color)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        
        c.set_line_width(px2f(cnf.base.w, cnf.border.thickness))
        print("thickness:", thickness)

        c.rectangle(x, y, w, h)

        c.stroke()

    def groove(self, cnf):
        c = self.c
        inset = cnf.groove.inset
        inset_f = px2f(cnf.base.w, inset)
        x = cnf.flat['panel.x']
        y = cnf.flat['panel.y']
        w = cnf.flat['panel.w']
        h = cnf.flat['panel.h']

        x = x + inset_f
        y = y + inset_f
        h = h - (inset_f * 2)
        w = w - (inset_f * 2)

        # Darken stroke to 80%
        p_elev = cnf.flat['panel.elevation']
        elev_change = cnf.groove.elevation
        elev = p_elev + elev_change
        color = (elev, elev, elev)

        thickness = px2f(cnf.base.w, cnf.groove.thickness)
        # setup stroke
        c.set_source_rgb(*color)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        
        c.set_line_width(px2f(cnf.base.w, cnf.groove.thickness))
        print("thickness:", thickness)

        c.rectangle(x, y, w, h)

        c.stroke()

    def roundrect(self, spec=None, rnd=None, r=0.0):
        cr = self.c
        x = rnd.spec.x
        y = rnd.spec.y
        from math import pi
        # width = rnd.spec.w
        # height = rnd.spec.h
        spec = rnd.spec
        cr.set_source_rgb(spec.fill_rgb[0], spec.fill_rgb[1], spec.fill_rgb[2])
        a, b, c, d = (0.25, 0.25, 0.5, 0.5)
        cr.arc(a + r, c + r, r, 2 * (pi / 2), 3 * (pi / 2))
        cr.arc(b - r, c + r, r, 3 * (pi / 2), 4 * (pi / 2))
        cr.arc(b - r, d - r, r, 0 * (pi / 2), 1 * (pi / 2))  # ;o)
        cr.arc(a + r, d - r, r, 1 * (pi / 2), 2 * (pi / 2))
        cr.close_path()
        cr.stroke()
        cr.fill()
