"""
Stores the information about state of game. Also valid moves for curr states. Keeps track of moves.
"""

class GameState():
  def __init__(self):
    #Board 8x8 2d list, 2 char each element, b or w then peice type Q,K,B ect..
    #two dash "--" means empty space.
    self.board =[
      ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],]
    self.whiteMove = True
    self.moveLog = []