"""
Python Main driver file. Handles the user input and shows gamestate obj information.
"""

from time import clock_getres
import pygame as p
from torch import true_divide
import ChessEngine
import os

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
    IMAGES[piece] = p.transform.scale(p.image.load("/img" + piece + ".png"), (SQ_SIZE,SQ_SIZE))



#handle input and graphics

def main():
    p.init()
    
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            clock.tick(MAX_FPS)
            p.display.flip()
            drawGameState(screen,gs)


#draws all graphics
def drawGameState(screen,gs):
  drawBoard(screen) #squares
  drawPieces(screen,gs.board) #pieces

#top left is always white
def drawBoard(screen):
  colors = [p.Color("white"), p.Color("gray")]
  for r in range(DIMENSION):
    for c in range(DIMENSION):
         color = colors[((r+c)%2)]
         p.draw.rect(screen,color,p.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def drawPieces(screen,board):
  pass

if __name__ == "__main__":
 main()