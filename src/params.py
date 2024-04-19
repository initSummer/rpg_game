#
# Author        : summer
# Description   :  params
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

screen_w = 20
screen_h = 15

cell_w = 32
cell_h = 32

hero_w = cell_w
hero_h = cell_h

screen_w_p = screen_w * cell_w
screen_h_p = screen_h * cell_h

rpg_home_dir = "/home/yxy/rpg_game"

developer_mode = True


class debug:
    if developer_mode:
        a_star = True
    else:
        a_star = False
