from typing import overload
from panelgen import config
from panelgen.utils import *
from panelgen.panels import Panel
from box import Box
import operator as op
from panelgen.config import load_config
from panelgen.config import g
from pprint import pprint
from panelgen.random import randomize
from panelgen.draw import wrap_texture
from PIL import Image, ImageChops

class Generator(object):
    def __init__(self, config) -> None:
        super().__init__()
        self.cnf = load_config(config)
        self.panel = Panel(self.cnf)
    
    @overload
    def generate(self, ptype):
        cnf = self.cnf

        # Type configuration
        tcnf = cnf['types'][ptype]
        tcnf.rand = config.make_flat(tcnf)
        print(tcnf)

        for i in range(cnf.base.count):
            print(tcnf[ptype])
            if tcnf[ptype].draw:
                print("drawing panel")
                self.panel.wrap_rect(tcnf)

            # self.panel.angled(cnf)
            
                # if tcnf['border'].draw:
                #     self.panel.border(tcnf)

            # if cnf.groove.draw:
            #     self.panel.groove(cnf)
            
            tcnf = randomize(tcnf)
        
        self.panel.save()

class TextureTileGenerator(Generator):
    def __init__(self, config) -> None:
        super().__init__(config)

    def generate(self, ptype):

        # Get config for the right type
        cnf = self.cnf
        tcnf = cnf['types'][ptype]
        tcnf.rand = config.make_flat(tcnf)

        # Create base image
        base = Image.new('RGBA', (cnf.base.w, cnf.base.h))

        # Load Texture to tile
        print("Loading texture:", tcnf[ptype].input)
        tex = Image.open(tcnf[ptype].input)

        # Render texture
        count = cnf.base.count
        
        for i in range(1, count+1):
            print(f"Iteration: [{i}/{count}]")

            # extract randomized settings
            x = tcnf.rand['texture.x']
            y = tcnf.rand['texture.y']
            w = tcnf.rand['texture.w']
            h = tcnf.rand['texture.h']

            # perform image wrapping
            wrap_texture(base, tex, x, y, tcnf)
            
            # Randomize settings
            tcnf = randomize(tcnf)

        # Save image
        base.save(tcnf.texture.output)
        print("Image saved:", tcnf.texture.output)
