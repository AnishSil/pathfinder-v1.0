import pygame
import math
from queue import PriorityQueue


WIDTH = 800
HEIGHT = 800

COLOR_START = (0, 255, 0)
COLOR_END = (255, 0, 0)
COLOR_BARRIER = (0, 0, 0)
COLOR_PATH = (255, 0, 255)
COLOR_EMPTY = (255, 255, 255)
COLOR_CLOSE = (120, 0, 0)
COLOR_OPEN = (0, 0, 255)
COLOR_LINE = (120, 120, 120)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")



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
    



def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()


def make_grid(rows, cols, width, height):
    grid =[]
    gap = min(width, height )// rows
    for x in range(rows):
        grid.append([])
        for y in range(cols):
            spot = Spot(x, y, gap, gap, rows, cols)
            grid[x].append(spot)

    return grid


def draw_grid(win, rows, cols, width, height):
    gap = width // rows
    for x in range(rows):
        pygame.draw.line(win, COLOR_LINE, (0, x * gap), (width, x * gap))
        for y in range(rows):
            pygame.draw.line(win, COLOR_LINE, (y * gap, 0), (y * gap, height))

def draw(win, grid, rows, cols, width, height):
    win.fill(COLOR_EMPTY)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, cols, width, height)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width //rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width, height):
    ROWS = 50
    COLS = 50
    grid = make_grid(ROWS, COLS, width, height)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, COLS, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start() 

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neigbors(grid)
                    
                    algorithm(lambda: draw(win, grid, ROWS, COLS, width, height), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS, width, height)

    pygame.quit()

main(WIN, WIDTH, HEIGHT)
