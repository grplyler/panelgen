import click
from PyQt5 import QtWidgets, uic
import matplotlib.image as mpimg
from panelgen.utils import *
from panelgen.generator import Generator, TextureTileGenerator
from panelgen.gui.mainwindow import MainWindow
from panelgen.normals import heightMapToNormalMap

@click.group()
def cli():
    pass


@cli.command(help="Generate a tiled heightmap from texture")
@click.option('--input', '-i', help="image texture to file")
@click.option('--size', '-s', help="image size (1024, 2048, etc)")
@click.option('--config', '-c', help="config.yml file", default="config.yml")
@click.option('--count', '-n', help="number of iterations", type=int)
@click.option('--output', '-o', help="output file (PNG)", default="out.png")
def tile(input, size, config, count, output):
    print("Loading texture:", input)
    gen = TextureTileGenerator(config)
    gen.cnf.base.count = count
    gen.cnf.types.texture.texture.output = output
    gen.cnf.types.texture.texture.input = input
    gen.generate('texture')

@cli.command(help="Generate a normal map from a heightmap")
@click.option('--input', '-i', help="height map png")
@click.option('--output', '-o', help="output file (PNG)", default="normal.png")
def normal(input, output):
    print("Generating normal map...")
    norm = heightMapToNormalMap(input)
    print("output:", output)
    mpimg.imsave(output, norm)

    print("Normal map saved:", output)

# @cli.command()
# @cli.option('--config', '-c', help="config.yml")
# @cli.option('--size', '-s', default=1024, help="size of generated heightmap")
# @cli.option('--count', '-n', default=12, help="number of iterations")
# @cli.option('--gui', '-g', default=False, is_flag=True, help="Use graphical user interface")
# def generate(paneltype, config, size, count, gui):
#     """A Height map and Normal Map Generator for Sci-fi panels"""
#     print("config:", config)
#     gen = Generator(config)

#     # Pull some configuration from command line
#     gen.cnf.base.type = paneltype
#     gen.cnf.base.w = size
#     gen.cnf.base.h = size
#     gen.cnf.base.count = count
#     gen.cnf.types[paneltype].count = count
#     print(gen.cnf)

#     # If we wanted a gui, launch it
#     print(gui)
#     if gui:
#         app = QtWidgets.QApplication(argv)
#         window = MainWindow(gen)
#         window.show()
#         app.exec_()

#     gen.generate('panel')

# cli.add_command(generate)
if __name__ == "__main__":
    cli()
