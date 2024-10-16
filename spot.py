import pygame
from colors import COLOR_EMPTY
from colors import COLOR_CLOSE
from colors import COLOR_OPEN
from colors import COLOR_BARRIER
from colors import COLOR_START
from colors import COLOR_END
from colors import COLOR_PATH

class Spot:
    def __init__(self, row, col, width, height, total_rows, total_cols) -> None:
        self.row = row
        self.col = col
        self.x = row * height
        self.y = col * width
        self.color = COLOR_EMPTY
        self.neighbors = []
        self.height = height
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == COLOR_CLOSE
    
    def is_open(self):
        return self.color == COLOR_OPEN

    def is_barrier(self):
        return self.color == COLOR_BARRIER
    
    def is_start(self):
        return self.color == COLOR_START
    
    def is_end(self):
        return self.color == COLOR_END
    
    def reset(self):
        self.color = COLOR_EMPTY
    
    def make_closed(self):
        self.color = COLOR_CLOSE
    
    def make_open(self):
        self.color = COLOR_OPEN

    def make_barrier(self):
        self.color = COLOR_BARRIER
    
    def make_start(self):
        self.color = COLOR_START
    
    def make_end(self):
        self.color = COLOR_END
    
    def make_path(self):
        self.color = COLOR_PATH


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_neigbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_barrier(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        
    def __lt__(self, other):
        return False
    

