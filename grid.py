import pygame
from spot import Spot
from colors import COLOR_LINE
from colors import COLOR_EMPTY


class Grid():
    def __init__(self) -> None:
        pass

    def make_grid(self, rows, cols, width, height):
        grid =[]
        gap = min(width, height )// rows
        for x in range(rows):
            grid.append([])
            for y in range(cols):
                spot = Spot(x, y, gap, gap, rows, cols)
                grid[x].append(spot)

        return grid


    def draw_grid(self,win, rows, cols, width, height):
        gap = width // rows
        for x in range(rows):
            pygame.draw.line(win, COLOR_LINE, (0, x * gap), (width, x * gap))
            for y in range(rows):
                pygame.draw.line(win, COLOR_LINE, (y * gap, 0), (y * gap, height))

    def draw(self,win, grid, rows, cols, width, height):
        win.fill(COLOR_EMPTY)

        for row in grid:
            for spot in row:
                spot.draw(win)

        self.draw_grid(win, rows, cols, width, height)
        pygame.display.update()


