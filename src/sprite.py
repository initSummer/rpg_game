#
# Author        : summer
# Description   :  sprite
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

import src.params as params


class Sprite:
    @staticmethod
    def draw(dest, source, x, y, cell_x, cell_y) -> None:
        dest.blit(source, (x, y), (cell_x * params.hero_w, cell_y * params.hero_h, params.hero_w, params.hero_h))
