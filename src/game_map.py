#
# Author        : summer
# Description   :  game map
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

import pygame

from src.array2d import Array2D
import src.params as params


class GameMap(Array2D):
    def __init__(self, bottom, top, x: int, y: int) -> None:
        width = int(bottom.get_width() / params.cell_w) + 1
        height = int(bottom.get_height() / params.cell_h) + 1
        super().__init__(width, height)
        if params.developer_mode:
            print(f"load map, size: ({width}, {height})")
        self.bottom_ = bottom
        self.top_ = top
        self.x_ = x
        self.y_ = y

    def draw_bottom(self, screen_surf):
        screen_surf.blit(self.bottom_, (self.x_, self.y_))

    def draw_top(self, screen_surf):
        screen_surf.blit(self.top_, (self.x_, self.y_))

    def load_walk_file(self, mapfile_path):
        with open(mapfile_path, 'r') as file:
            lines = file.readlines()
            for y in range(self.height_):
                line = lines[y]
                line = line.strip()
                cells = line.split(',')
                for x in range(self.width_):
                    self[x][y] = float(cells[x])
        self.show_array2d()

    def draw_grid(self, screen_surf):
        for x in range(self.width_):
            for y in range(self.height_):
                if self[x][y] == 0:
                    pygame.draw.rect(screen_surf, (255, 255, 255), (self.x_ + x * params.cell_w, self.y_ + y * params.cell_h, params.cell_w, params.cell_h), 1)
                else:
                    pygame.draw.rect(screen_surf, (0, 0, 0), (self.x_ + x * params.cell_w + 1, self.y_ + y * params.cell_h + 1, params.cell_w - 2, params.cell_h - 2), 0)
