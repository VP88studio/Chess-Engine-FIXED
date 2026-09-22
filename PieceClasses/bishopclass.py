import pygame, math, sys, time, os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from imgrenderer import loadimgs
loadimgs()
placeholderimg = 0
class bishopclass():
    def __init__(self):
        self.color = 3
        self.img = placeholderimg
        self.startpos = 0
        self.pos = self.startpos
        self.status = "Alive"
