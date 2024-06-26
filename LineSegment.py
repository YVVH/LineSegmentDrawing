"""
线段类
"""
import math


class LineSegment:
    """
    point1:起点坐标
    point2:终点坐标
    x2:终点横坐标
    slope:斜率
    """

    # 支持两种构造方法
    def __init__(self, *args):
        # 使用端点构造
        if len(args) == 2:
            self.point1, self.point2 = args
            x1, y1 = round(self.point1[0]), round(self.point1[1])
            x2, y2 = round(self.point2[0]), round(self.point2[1])
            self.point1, self.point2 = (x1, y1), (x2, y2)
            delta_x = x2 - x1
            delta_y = y2 - y1
            if delta_y == 0:
                self.slope = 0
                self.angle = 0
            elif delta_x == 0:  # 避免除以0
                if delta_y > 0:
                    self.angle = 90
                    self.slope = float('inf')
                elif delta_y < 0:
                    self.angle = -90
                    self.slope = float('-inf')
            else:
                self.slope = delta_y / delta_x
                self.angle = math.degrees(math.atan(self.slope))

        # 使用起点角度终点deltax构造
        elif len(args) == 3:
            self.point1, delta, self.angle = args
            x1, y1 = round(self.point1[0]), round(self.point1[1])
            self.point1 = (x1, y1)
            if 0 < self.angle < 90 or 90 < self.angle < 180 or -90 < self.angle < 0 or -180 < self.angle < -90:
                self.slope = math.tan(math.radians(self.angle))
                y2 = y1 + self.slope * delta
                self.point2 = (x1 + delta, y2)
            elif self.angle == 90:
                y2 = y1 + delta
                self.slope = float('inf')
                self.point2 = (x1, y2)
            elif self.angle == 0:
                x2 = x1 + delta
                self.slope = 0
                self.point2 = (x2, y1)
            elif self.angle == -90:
                y2 = y1 - delta
                self.slope = float('-inf')
                self.point2 = (x1, y2)
            elif self.angle == 180 or self.angle == -180:
                x2 = x1 - delta
                self.slope = 0
                self.point2 = (x2, y1)
            x2, y2 = round(self.point2[0]), round(self.point2[1])
            self.point2 = (x2, y2)
        else:
            raise ValueError("Invalid arguments for LineSegment constructor")

        self.coor_list = self.get_coor()

    def get_coor(self):
        """
        根据端点求出直线上每个点的坐标
        """
        x1, y1 = round(self.point1[0]), round(self.point1[1])
        x2, y2 = round(self.point2[0]), round(self.point2[1])
        # 根据端点以及斜率取点，每个点间隔0.2
        if self.angle == 90:
            corr_list = [(x1, y) for y in range(y1, y2 + 1)]
        elif self.angle == -90:  # 目前没有这种情况
            corr_list = [(x1, y) for y in range(y2, y1 - 1, -1)]
        elif self.angle == 0:
            corr_list = [(x, y1) for x in range(x1, x2 + 1)]
        elif self.angle == 180 or self.angle == -180:
            corr_list = [(x, y1) for x in range(x2, x1 + 1, -1)]
        else:
            corr_list = [(x, y1 + (x - x1) * self.slope) for x in range(x1, x2 + 1)]

        return corr_list
