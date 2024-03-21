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

    def __init__(self, point1, x2=None, angle=None, point2=None):
        self.point1 = point1
        if point2 is None:
            self.angle = angle
            if -90 < angle < 90 and angle != 0:
                self.radians = math.radians(angle)  # 角度转弧度
                self.point2 = (x2, self.point1[1] + (x2 - self.point1[0]) * math.tan(self.radians))
            elif angle == 90:  # 垂直时，x2为长度
                self.point2 = (self.point1[0], self.point1[1] + x2)
            elif angle == -90:
                self.point2 = (self.point1[0], self.point1[1] - x2)
            elif angle == 0:
                self.point2 = (self.point1[0] + x2, self.point1[1])
        else:
            if angle is None:
                self.point2 = point2
            else:
                self.angle = self.angle

        self.coor_list = self.get_coor(angle)


    def get_coor(self, angle):
        """
        根据端点求出直线上每个点的坐标
        """
        corr_list = []
        x0, y0 = round(self.point1[0]), round(self.point1[1])
        x1, y1 = round(self.point2[0]), round(self.point2[1])
        # 根据端点以及斜率取点，每个点间隔0.2
        if angle == 90:
            corr_list = [(x0, y / 5) for y in range((y0 * 5), (y1 + 1) * 5)]
        elif angle == -90:  # 目前没有这种情况
            corr_list = []
        elif angle == 0:
            corr_list = [(x / 5, y0) for x in range((x0 * 5), (x1 + 1) * 5)]

        return corr_list


    def get_slope(self):
        """计算并返回线段的斜率"""
        x1, y1 = self.point1
        x2, y2 = self.point2
        # 计算斜率
        delta_x = x2 - x1
        if delta_x == 0:  # 避免除以0
            return float('inf')  # 斜率无穷大，线段是垂直的
        return (y2 - y1) / delta_x
