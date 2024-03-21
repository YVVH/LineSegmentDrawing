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
    def __init__(self, *args):
        # 使用端点构造
        if len(args) == 2:
            self.point1, self.point2 = args
            x1, y1 = self.point1
            x2, y2 = self.point2
            delta_x = x2 - x1
            delta_y = y2 - y1
            if delta_y == 0:
                self.slope = 0
                self.angle = 0
            elif delta_x == 0:  # 避免除以0
                if delta_y > 0:
                    self.angle = 90
                elif delta_y < 0:
                    self.angle = -90
            else:
                self.slope = delta_y / delta_x
                self.angle = math.degrees(math.atan(self.slope))

        # 使用起点角度终点deltax构造
        elif len(args) == 3:
            self.point1, delta, self.angle = args
            x1, y1 = self.point1
            if 0 < self.angle < 90:
                self.slope = math.tan(math.radians(self.angle))
                y2 = y1 + math.sin(math.radians(self.angle)) * delta
                self.point2 = (x1 + delta, y2)
            elif self.angle == 90:
                y2 = y1 + delta
                self.slope = float('inf')
                self.point2 = (x1, y2)
            elif self.angle == 0:
                x2 = x1 + delta
                self.slope = 0
                self.point2 = (x2, y1)
        else:
            raise ValueError("Invalid arguments for LineSegment constructor")

        self.coor_list = self.get_coor()

    def get_coor(self):
        """
        根据端点求出直线上每个点的坐标
        """
        x0, y0 = round(self.point1[0]), round(self.point1[1])
        x1, y1 = round(self.point2[0]), round(self.point2[1])
        # 根据端点以及斜率取点，每个点间隔0.2
        if self.angle == 90:
            corr_list = [(x0, y / 5) for y in range((y0 * 5), (y1 * 5 + 1))]
        elif self.angle == -90:  # 目前没有这种情况
            corr_list = []
        elif self.angle == 0:
            corr_list = [(x / 5, y0) for x in range((x0 * 5), (x1 * 5 + 1))]
        else:
            corr_list = [(x / 5, y0 + (x / 5 - x0) * self.slope) for x in range((x0 * 5), (x1 * 5 + 1))]

        return corr_list
