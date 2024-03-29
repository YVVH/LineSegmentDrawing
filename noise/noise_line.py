import random

import cv2
from LineSegment import LineSegment

delta_x_lower = 10
delta_x_upper = 15
line_offset_lower, line_offset_upper = -2, 2

class NoiseLine:
    def __init__(self, point, angle, line_number, x_limit, y_limit):
        self.point = point
        self.angle = angle
        self.line_list = []
        point0 = (self.point[0] + random.uniform(line_offset_lower, line_offset_upper), self.point[1] +
                  random.uniform(0, 5))
        angle_lower = -20  # 像素坐标是反转的，因此角度为负值
        angle_upper = -75
        for _ in range(line_number):
            delta_x = random.uniform(delta_x_lower, delta_x_upper)
            angle = random.uniform(angle_lower, angle_upper)
            # print(angle)
            line = LineSegment(point0, delta_x, angle)
            if line.point2[0] > x_limit:
                delta_x = x_limit - line.point2[0]
                line = LineSegment(point0, delta_x, angle)
            if line.point2[1] < y_limit:
                line = LineSegment(point0, (point0[0] + delta_x, y_limit))

            self.line_list.append(line)
            point0 = line.point2
            angle_upper = angle  # 递减

    def draw(self, image, color, thickness=1):
        for line in self.line_list:
            cv2.line(image, line.point1, line.point2, color, thickness)
