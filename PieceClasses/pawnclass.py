import pygame, math, sys, time, os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from imgrenderer import loadimgs
loadimgs()
class pawn():
    def __init__(self):
        self.color = 3
        if self.color == 0:
            self.img = bpawnimg
        if self.color == 1:
            self.img = wpawnimg
        self.startpos = 0
        self.pos = self.startpos
        self.status = "Alive"
