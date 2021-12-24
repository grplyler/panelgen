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

class Generator(object):
    def __init__(self, config) -> None:
        super().__init__()
        self.cnf = load_config(config)
        self.panel = Panel(self.cnf)
    
    def generate(self, ptype):
        cnf = self.cnf

        # Type configuration
        tcnf = cnf['types'][ptype]
        tcnf.flat = config.make_flat(tcnf)
        print(tcnf)

        for i in range(cnf.base.count):
            print(tcnf[ptype])
            if tcnf[ptype].draw:
                print("drawing panel")
                self.panel.rect(tcnf)

            # self.panel.angled(cnf)
            
                # if tcnf['border'].draw:
                #     self.panel.border(tcnf)

            # if cnf.groove.draw:
            #     self.panel.groove(cnf)
            
            tcnf = randomize(tcnf)
        
        self.panel.save()
        # self.panel.display('out.png')
