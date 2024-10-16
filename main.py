import pygame
from grid import Grid
from helper import Helper
from algorithms import Solver


WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

get_clicked_pos = lambda pos, rows, width: Helper().get_clicked_pos(pos, rows, width)

a_star = lambda draw, grid, start, end: Solver().a_star(draw, grid, start, end)

make_grid = lambda rows, cols, width, height: Grid().make_grid(rows, cols, width, height)
draw_grid = lambda win, rows, cols, width, height: Grid().draw_grid(win, rows, cols, width, height)
draw = lambda win, grid, rows, cols, width, height: Grid().draw(win, grid, rows, cols, width, height)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

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
                    
                    a_star(lambda: draw(win, grid, ROWS, COLS, width, height), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS, width, height)

    pygame.quit()

main(WIN, WIDTH, HEIGHT)
