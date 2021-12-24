import click
from PyQt5 import QtWidgets, uic
from sys import argv

from panelgen.utils import *
from panelgen.generator import Generator
from panelgen.gui.mainwindow import MainWindow


@click.command()
@click.argument('paneltype')
@click.option('--config', '-c', help="config.yml")
@click.option('--size', '-s', default=1024, help="size of generated heightmap")
@click.option('--count', '-n', default=12, help="number of iterations")
@click.option('--gui', '-g', default=True, is_flag=True, help="Use graphical user interface")
def generate(paneltype, config, size, count, gui):
    """A Height map and Normal Map Generator for Sci-fi panels"""
    print("config:", config)
    gen = Generator(config)

    # Pull some configuration from command line
    gen.cnf.base.type = paneltype
    gen.cnf.base.w = size
    gen.cnf.base.h = size
    gen.cnf.base.count = count
    gen.cnf.types[paneltype].count = count
    print(gen.cnf)

    # If we wanted a gui, launch it
    print(gui)
    if gui:
        app = QtWidgets.QApplication(argv)
        window = MainWindow(gen)
        window.show()
        app.exec_()
    # gen.generate('panel')

if __name__ == "__main__":
    generate()
