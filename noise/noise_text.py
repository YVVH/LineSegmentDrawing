import cv2
from LineSegment import LineSegment
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math
from noise.noise_circle import Circle


class X:
    """
    :param center: 中心点的坐标，以(x, y)的形式表示。
    :param length: 从中心点开始延申四条线段的长度
    """
    def __init__(self, center, length):
        self.center = center
        self.length = length

    def draw(self, image, color, thickness=1):
        # 从起点开始，延申四条线
        delta_x = self.length * math.sin(math.pi / 4)
        line1 = LineSegment(self.center, -delta_x, 135)
        line2 = LineSegment(self.center, -delta_x, -135)
        line3 = LineSegment(self.center, delta_x, 45)
        line4 = LineSegment(self.center, delta_x, -45)

        # 绘制线段
        start_point = self.center
        end_point1 = tuple(round(x) for x in line1.point2)
        end_point2 = tuple(round(x) for x in line2.point2)
        end_point3 = tuple(round(x) for x in line3.point2)
        end_point4 = tuple(round(x) for x in line4.point2)
        cv2.line(image, start_point, end_point1, color, thickness)
        cv2.line(image, start_point, end_point2, color, thickness)
        cv2.line(image, start_point, end_point3, color, thickness)
        cv2.line(image, start_point, end_point4, color, thickness)

    def draw_X_plus(self, image, color, thickness=1):
        # 从起点开始，延申四条线
        delta_x = self.length * math.sin(math.pi / 4)
        line1 = LineSegment(self.center, -delta_x, 135)
        line2 = LineSegment(self.center, -delta_x, -135)
        line3 = LineSegment(self.center, delta_x, 45)
        line4 = LineSegment(self.center, delta_x, -45)

        # 绘制线段
        start_point = self.center
        end_point1 = tuple(round(x) for x in line1.point2)
        end_point2 = tuple(round(x) for x in line2.point2)
        end_point3 = tuple(round(x) for x in line3.point2)
        end_point4 = tuple(round(x) for x in line4.point2)
        cv2.line(image, start_point, end_point1, color, thickness)
        cv2.line(image, start_point, end_point2, color, thickness)
        cv2.line(image, start_point, end_point3, color, thickness)
        cv2.line(image, start_point, end_point4, color, thickness)

        # 画点
        mid_point1 = (round((line1.point2[0] + line2.point2[0]) / 2), round((line1.point2[1] + line2.point2[1]) / 2))
        mid_point2 = (round((line2.point2[0] + line4.point2[0]) / 2), round((line2.point2[1] + line4.point2[1]) / 2))
        mid_point3 = (round((line3.point2[0] + line4.point2[0]) / 2), round((line3.point2[1] + line4.point2[1]) / 2))
        mid_point4 = (round((line1.point2[0] + line3.point2[0]) / 2), round((line1.point2[1] + line3.point2[1]) / 2))
        c1 = Circle(mid_point1, radius=1)
        c2 = Circle(mid_point2, radius=1)
        c3 = Circle(mid_point3, radius=1)
        c4 = Circle(mid_point4, radius=1)
        c1.draw(image, color, thickness)
        c2.draw(image, color, thickness)
        c3.draw(image, color, thickness)
        c4.draw(image, color, thickness)

class Character:
    def __init__(self, center, text, font_size):
        """
            :param center: 中心点的坐标，以(x, y)的形式表示。
            :param text: 需要显示的字符
        """
        self.text = text
        self.center = center
        self.font_size = font_size

    def draw(self, image, color):
        """
        :param image:
        :return:
        """
        pilimg = Image.fromarray(image)
        img_draw = ImageDraw.Draw(pilimg)
        font = ImageFont.truetype('simsun.ttc', self.font_size, encoding="utf-8")
        img_draw.text(self.center, text=self.text, fill=color, font=font)
        # PIL图片转cv2 图片
        return cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
