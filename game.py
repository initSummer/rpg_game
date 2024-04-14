#
# Author        : summer
# Description   : rpg game starter
# 
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
# 

import sys
import pygame

from src.sprite import Sprite
from src.game_map import GameMap
from src.char_walk import CharWalk
import src.params as params
from src.a_star import Point


class Game:
    def __init__(self, title: str, width: int, height: int, fps: int = 60) -> None:
        self.title_ = title
        self.width_ = width
        self.height_ = height
        self.fps_ = fps

        self.screen_surf_ = None
        self.clock_ = None

        self._init_pygame()
        self._init_game()
        self._update()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title_)
        self.screen_surf_ = pygame.display.set_mode([self.width_, self.height_])
        self.clock_ = pygame.time.Clock()

    def _init_game(self):
        self.hero_ = pygame.image.load(f'{params.rpg_home_dir}/data/img/character/heros_0.png').convert_alpha()
        self.map_bottom = pygame.image.load(f'{params.rpg_home_dir}/data/img/map/map_0_bottom.png').convert_alpha()
        self.map_top = pygame.image.load(f'{params.rpg_home_dir}/data/img/map/map_0_top.png').convert_alpha()
        self.game_map_ = GameMap(self.map_bottom, self.map_top, 0, 0)
        self.game_map_.load_walk_file(f'{params.rpg_home_dir}/data/map/0_2d.map')
        # self.game_map_.load_walk_file(f'{params.rpg_home_dir}/data/map/0.map')
        self.role_ = CharWalk(self.hero_, 0, CharWalk.DIR_DOWN, 5, 10)
        self.role_.goto(14, 10)

    def _update(self):
        while True:
            self.clock_.tick(self.fps_)

            self.role_.move()
            self.role_.logic()
            self._event_handler()

            self.game_map_.draw_bottom(self.screen_surf_)
            self.role_.draw(self.screen_surf_, self.game_map_.x_, self.game_map_.y_)
            self.game_map_.draw_top(self.screen_surf_)

            self.game_map_.draw_grid(self.screen_surf_)

            pygame.display.update()

    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mx = (mouse_x - self.game_map_.x_) // params.cell_w
                my = (mouse_y - self.game_map_.y_) // params.cell_h
                if params.debug.a_star:
                    print(f"try to find path, mouse: ({mouse_x // params.cell_w}, {mouse_y // params.cell_h})")
                    print(f"  game_map: ({self.game_map_.x_ // params.cell_w}, {self.game_map_.y_ // params.cell_h})")
                    print(f"  start_point: ({self.role_.mx_}, {self.role_.my_})")
                self.role_.find_path(self.game_map_, Point(mx, my))


if __name__ == '__main__':
    Game("rpg", params.screen_w_p, params.screen_h_p)
