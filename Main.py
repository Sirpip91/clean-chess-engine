"""
Python Main driver file. Handles the user input and shows gamestate obj information.
"""

import pygame as p
import ChessEngine

#define spacing
WIDTH = HEIGHT = 512
DIMENSION = 8 
SQ_SIZE = HEIGHT //DIMENSION
MAX_FPS = 15
IMAGES = {}

# Load images once for pythons sake
#INIT global group of images to call into main.
def loadImages():
  #IMAGES ['wP'] = p.image.load("img/wP.png")
  pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP','bR','bN','bB','bK','bQ']
  for piece in pieces:
    IMAGES[piece] = p.transform.scale(p.image.load("img/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))



#handle input and graphics

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs)
  