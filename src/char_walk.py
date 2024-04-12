#
# Author        : summer
# Description   :  character walk
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

from src.sprite import Sprite
import src.params as params


class CharWalk:
    DIR_DOWN = 0
    DIR_LEFT = 1
    DIR_RIGHT = 2
    DIR_UP = 3

    def __init__(self, hero_surf, char_id, dir, mx, my):
        self.hero_surf_ = hero_surf
        self.char_id_ = char_id
        self.dir_ = dir
        self.mx_ = mx
        self.my_ = my

        self.is_walking_ = False
        self.frame_ = 1
        self.x_ = self.mx_ * 32
        self.y_ = self.my_ * 32

        self.next_mx_ = 0
        self.next_my_ = 0

        self.step_ = 2

    def draw(self, screen_surf, map_x, map_y):
        cell_x = self.char_id_ % 12 + int(self.frame_)
        cell_y = self.char_id_ // 12 + self.dir_
        Sprite.draw(screen_surf, self.hero_surf_, map_x + self.x_, map_y + self.y_, cell_x, cell_y)

    def goto(self, x, y):
        self.next_mx_ = x
        self.next_my_ = y

        if self.next_mx_ > self.mx_:
            self.dir_ = CharWalk.DIR_RIGHT
        elif self.next_mx_ < self.my_:
            self.dir_ = CharWalk.DIR_LEFT
        elif self.next_my_ > self.my_:
            self.dir_ = CharWalk.DIR_DOWN
        elif self.next_my_ < self.my_:
            self.dir_ = CharWalk.DIR_UP

        self.is_walking_ = True

    def move(self):
        if not self.is_walking_:
            return
        dest_x = self.next_mx_ * params.cell_w
        dest_y = self.next_my_ * params.cell_h

        if self.x_ < dest_x:
            self.x_ += self.step_
            if self.x_ > dest_x:
                self.x_ = dest_x
        elif self.x_ > dest_x:
            self.x_ -= self.step_
            if self.x_ < dest_x:
                self.x_ = dest_x

        if self.y_ < dest_y:
            self.y_ += self.step_
            if self.y_ > dest_y:
                self.y_ = dest_y
        elif self.y_ > dest_y:
            self.y_ -= self.step_
            if self.y_ < dest_y:
                self.y_ = dest_y

        self.frame_ = (self.frame_ + 0.1) % 3

        self.mx_ = int(self.x_ / params.cell_w)
        self.my_ = int(self.y_ / params.cell_h)

        if self.x_ == dest_x and self.y_ == dest_y:
            self.frame_ = 1
            self.is_walking_ = False
