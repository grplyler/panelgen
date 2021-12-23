from typing import overload
from panelgen.utils import *
from panelgen.panels import Panel
from box import Box
import operator as op
from panelgen.config import load_config
from panelgen.config import g
from pprint import pprint
from panelgen.random import randomize

class Generator(object):
    def __init__(self) -> None:
        super().__init__()
        self.cnf = load_config('panelgen/config.yml')
        self.panel = Panel(self.cnf)
    
    def generate(self):
        cnf = self.cnf
        for i in range(cnf.panel.count):
            self.panel.rect(cnf)
            
            if cnf.border.draw:
                self.panel.border(cnf)

            if cnf.groove.draw:
                self.panel.groove(cnf)
            
            cnf = randomize(cnf)
        
        self.panel.save()
        self.panel.display('out.png')
