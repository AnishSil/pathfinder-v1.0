import pygame

WIDTH  = 800
HEIGHT = 800

COLOR_START   = (255, 255, 255)
COLOR_END     = (255, 255, 255)
COLOR_BARRIER = (255, 255, 255)
COLOR_PATH    = (255, 255, 255)
COLOR_EMPTY   = (255, 255, 255)
COLOR_CLOSE   = (255, 255, 255)
COLOR_OPEN    = (255, 255, 255)

WIN = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Maze Runne")



class Spot:
    def __init__(self, row, col, width, height, total_rows) -> None:
        self.row = row
        self.col = col
        self.x = row * height
        self.y = col * width
        self.color = COLOR_EMPTY
        self.neighbors = []
        self.height = height
        self.width = width
        self.total_rows = total_rows

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
        self.color == COLOR_PATH


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_neigbors(self, grid):
        pass

    def __lt__(self,other):
        return False
    


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)