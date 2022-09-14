import random
import sys
import pygame as pg
import pygame.gfxdraw


def draw_pixel(screen, position: list, size: int, color: tuple) -> None:
    pygame.gfxdraw.box(screen, (position[0], position[1], size, size), color)


def draw_ant(screen, position, size):
    pygame.gfxdraw.box(screen, (position[0] * size, position[1] * size, size, size), (255, 0, 0))


def draw_field(screen, cells: list, size: int) -> None:
    for i, raw in enumerate(cells):
        for j, is_black in enumerate(raw):
            if is_black:
                draw_pixel(screen, [i * size, j * size], size, (0, 0, 0))


def main():
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((800, 800))
    pg.display.set_caption("Langton's Ant")

    cells = [[False for _ in range(100)] for _ in range(100)]

    ant_pos = [50, 50]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dir_i = 3

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        draw_field(screen, cells, 8)
        draw_ant(screen, ant_pos, 8)

        if not cells[ant_pos[0]][ant_pos[1]]:
            dir_i = (dir_i + 1) % 4
        else:
            dir_i = (dir_i - 1) % 4

        cells[ant_pos[0]][ant_pos[1]] = not cells[ant_pos[0]][ant_pos[1]]
        ant_pos = [(c + c1) % 100 for c, c1 in zip(ant_pos, directions[dir_i])]

        pg.display.flip()
        clock.tick(120)


if __name__ == '__main__':
    main()
