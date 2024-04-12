#
# Author        : summer
# Description   :  array 2d
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

import src.params as params


class Array2D:

    def __init__(self, width: int, height: int, default=0):
        self.width_ = width
        self.height_ = height
        self.data = [[default for y in range(self.height_)] for x in range(self.width_)]

    def show_array2d(self):
        for y in range(self.height_):
            for x in range(self.width_):
                print(self.data[x][y], end='')
            print("")

    def __getitem__(self, item):
        return self.data[item]
