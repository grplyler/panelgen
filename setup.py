from setuptools import setup, find_packages

setup(
    name="panelgen",
    description="A Height map and Normal Map Generator for Sci-fi panels",
    version="0.1",
    author="Ryan Plyler <g.r.plyler@gmail.com>",
    packages=find_packages(),
    install_requires=[
        "click",
        "PyQt5",
        "numpy",
        "matplotlib",
        "python-box",
        "opencv-python"
    ],
    entry_points={
        "console_scripts": [
            "panelgen = panelgen.cli:cli"
        ]
    },
)