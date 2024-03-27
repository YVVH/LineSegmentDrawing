import math
import cv2
import numpy as np
from LineSegment import LineSegment


class Triangle:
    def __init__(self, center, length):
        """
        初始化一个正三角形对象。

        :param center: 三角形中心点的坐标，以(x, y)的形式表示。
        :param length: 三角形的边长。
        """
        self.center = center
        self.length = length
        self.calculate_vertices()

    def calculate_vertices(self):
        """
        计算并设置三角形的顶点坐标。
        使用三角形外切圆的思路
        注意像素坐标y轴是倒过来的
        """
        # 计算三角形的顶点
        line1 = LineSegment(self.center, -self.length / 2, 90)
        line2 = LineSegment(self.center, -self.length / 2, -30)
        line3 = LineSegment(self.center, self.length / 2, -150)
        self.vertices = [line1.point2, line2.point2, line3.point2]

    def draw(self, image, color, thickness=1):
        """
        :param color: 三角形的颜色，以BGR格式表示。
        :param thickness: 线条的粗细。
        """
        cv2.line(image, self.vertices[0], self.vertices[1], color, thickness)
        cv2.line(image, self.vertices[1], self.vertices[2], color, thickness)
        cv2.line(image, self.vertices[2], self.vertices[0], color, thickness)
        # 绘制中心的点
        cv2.circle(image, self.center, 1, color, -1)
