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
                draw_pixel(screen, [i * 8, j * 8], size, (0, 0, 0))


def main():
    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((800, 800))
    pg.display.set_caption("Langton's Ant")

    cells = [[False for _ in range(100)] for _ in range(100)]

    ant_pos = [50, 50]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))

        draw_field(screen, cells, 8)
        draw_ant(screen, ant_pos, 8)

        ant_pos[0] = (ant_pos[0] + 1) % 100

        pg.display.flip()
        clock.tick(5)


if __name__ == '__main__':
    main()
