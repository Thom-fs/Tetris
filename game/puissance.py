import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

class Piece(object):
      rows = 20 # y
      columns = 10 # x

      def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shape.index(shape)]
            self.rotation= 0  # number 0-3


def create_grip(locked_position = {}):
      # _ or x its w/e
      grid = [[(0,0,0) for _ in range (10)] for _ in range (20)]
      #first list grip = 20
      for i in range (len(grid)):
            #2nd list grip = 10
            for j in range(len(grid[i])):
                  #j=x, i=y
                  if (j,i) in locked_position:
                        c = locked_position[(j,i)]
                        grid[i][j] = c
      return grid


def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return random.choice(shapes)

def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface, grid):
      # surface color : black
      surface.filll((0,0,0))

      pygame.font.init()
      font = pygame.font.SysFont('comicsans', 60)
      label = font.render('Tetris', 1, (255,255,255))

      #draw the label and get it in the middle of the screen
      surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))


      # loop trough every color within the grid i,j
      for i in range(len(grid)):
            for j in range(len(grid[id])):
                  # surface drawing on to, and the position, width and height with block size will change dynamically
                  pygame.draw.react(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size, 0))

      pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)

      pygame.display.update()


def clear_rows(grid, locked):
      pass

def draw_next_shape(shape, surface):
      pass

def draw_window(surface):
    pass

def main():
    pass

def main_menu():
    pass

main_menu()  # start game

