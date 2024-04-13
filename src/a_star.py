#
# Author        : summer
# Description   :  character walk
#
# Revision      :
# Rev.    Date        Designer    Description
# 1.0     2024-04-12  summer      Initial version
#

class Point:
    pass


class AStar:
    pass


class Point:
    def __init__(self, x: int, y: int):
        self.x_ = x
        self.y_ = y

    def x(self) -> int:
        return self.x_

    def y(self) -> int:
        return self.y_

    def __eq__(self, other: Point):
        return self.x_ == other.x() and self.y_ == other.y()

    def __str__(self):
        return f"({self.x()}, {self.y()})"


class AStar:
    class Node:
        def __init__(self, point: Point, end_point: Point, g=0):
            self.point_ = point
            self.father_ = None
            self.g_ = g
            self.h_ = (abs(end_point.x() - point.x()) + abs(end_point.y() - point.y())) * 10

    def __init__(self, map2d, start_point: Point, end_point: Point, pass_tag: int = 0):
        print(f"start_point type: {type(start_point)}")
        print(f"end_point type: {type(end_point)}")
        self.open_list_ = []
        self.close_list_ = []
        self.map2d_ = map2d
        if isinstance(start_point, Point) and isinstance(end_point, Point):
            self.start_point_ = start_point
            self.end_point_ = end_point
        else:
            self.start_point_ = start_point
            self.end_point_ = end_point
            # self.start_point_ = Point(*start_point)
            # self.end_point_ = Point(*end_point)

        self.pass_tag_ = pass_tag

    def get_min_node(self) -> Node:
        current_node = self.open_list_[0]
        for node in self.open_list_:
            if node.g_ + node.h_ < current_node.g_ + current_node.h_:
                current_node = node
        return current_node

    def point_in_close_list(self, point) -> bool:
        for node in self.close_list_:
            if node.point_ == point:
                return True
        return False

    def point_in_open_list(self, point) -> Node:
        for node in self.open_list_:
            if node.point_ == point:
                return node
        return None

    def end_point_in_close_list(self) -> Node:
        for node in self.open_list_:
            if node.point_ == self.end_point_:
                return node
        return None

    def search_near(self, min_f: Node, offset_x: int, offset_y: int):
        # check bound
        if min_f.point_.x() + offset_x < 0 or min_f.point_.x() + offset_x > self.map2d_.width_ - 1 \
                or min_f.point_.y() + offset_y < 0 or min_f.point_.y() + offset_y > self.map2d_.width_ - 1:
            return

        # check obstacle
        if self.map2d_[min_f.point_.x() + offset_x][min_f.point_.y() + offset_y] != self.pass_tag_:
            return

        # check visited
        current_point = Point(min_f.point_.x() + offset_x, min_f.point_.y() + offset_y)
        if self.point_in_close_list(current_point):
            return

        # set cost
        if offset_x == 0 and offset_y == 0:
            step = 10
        else:
            step = 14

        current_node = self.point_in_close_list(current_point)
        if not current_node:
            current_node = AStar.Node(current_point, self.end_point_, g=min_f.g_ + step)
            current_node.father_ = min_f
            self.open_list_.append(current_node)

        if min_f.g_ + step < current_node.g_:
            current_node.g_ = min_f.g_ + step
            current_node.father_ = min_f

    def start(self):
        # check obstacle
        if self.map2d_[self.end_point_.x()][self.end_point_.y()] != self.pass_tag_:
            return None

        start_node = AStar.Node(self.start_point_, self.end_point_)
        self.open_list_.append(start_node)
        while True:
            min_f = self.get_min_node()
            self.close_list_.append(min_f)
            self.open_list_.remove(min_f)
            self.search_near(min_f, 0, -1)
            self.search_near(min_f, 0, 1)
            self.search_near(min_f, 1, 0)
            self.search_near(min_f, -1, 0)

            point = self.end_point_in_close_list()
            if point:
                c_point = point
                path_list = []
                while True:
                    if c_point.father_:
                        path_list.append(c_point.point_)
                        c_point = c_point.father_
                    else:
                        return list(reversed(path_list))
            if len(self.open_list_) == 0:
                return None


if __name__ == "__main__":
    a = Point(1, 2)
    b = Point(3, 5)
    c = Point(1, 2)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"a = b: {a == b}")
    print(f"a = c: {a == c}")
