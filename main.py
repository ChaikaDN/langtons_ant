import sys
import pygame as pg
import pygame.gfxdraw


def draw_pixel(screen: pg.Surface, position: list, size: int, color: tuple) -> None:
    pygame.gfxdraw.box(screen, (position[0] * size, position[1] * size, size, size), color)


def draw_ant(screen: pg.Surface, position: list, size: int) -> None:
    draw_pixel(screen, position, size, (255, 0, 0))


def draw_field(screen, cells: list, size: int) -> None:
    for i, raw in enumerate(cells):
        for j, is_black in enumerate(raw):
            if is_black:
                draw_pixel(screen, [i, j], size, (0, 0, 0))


def main():
    window_size = (800, 800)
    shape = 200
    cell_size = window_size[0] // shape

    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode(window_size)
    pg.display.set_caption("Langton's Ant")

    cells = [[False for _ in range(shape)] for _ in range(shape)]
    ant_pos = [shape//2, shape//2]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dir_i = 3

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        draw_field(screen, cells, cell_size)
        draw_ant(screen, ant_pos, cell_size)

        if not cells[ant_pos[0]][ant_pos[1]]:
            dir_i = (dir_i + 1) % 4
        else:
            dir_i = (dir_i - 1) % 4

        cells[ant_pos[0]][ant_pos[1]] = not cells[ant_pos[0]][ant_pos[1]]
        ant_pos = [(c + c1) % shape for c, c1 in zip(ant_pos, directions[dir_i])]

        pg.display.flip()
        clock.tick(120)


if __name__ == '__main__':
    main()
