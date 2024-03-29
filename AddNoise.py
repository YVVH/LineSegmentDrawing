import random

import cv2
import numpy as np

from noise.noise_circle import Circle
from noise.noise_text import Character, X
from noise.noise_triangle import Triangle

noise_number = 20  # 噪声数量
noise_x_offset_lower = -10
noise_x_offset_upper = 10
noise_y_offset_lower = -10
noise_y_offset_upper = 10
circle_radius = 5  # 圆形的半径
triangle_length = 12  # 三角形中心点到端点的距离
X_length = 5  # 叉号的长度
font_size = 16  # 字体大小
character_list = ['上', '中', '下']  # 随机文本库
character_weight = [0.33, 0.33, 0.34]  # 随机文本权重
noise_type_list = [0, 1, 2, 3, 4]  # 0圆 1三角形 2X 3文本 4混合
noise_type_weight = [1, 0, 0, 0, 0]  # 噪声权重
noise_thickness_para = 1500
mixed_noise_x_offset = 8
mixed_noise_y_offset = -8


def get_noise_thickness(height, width):
    return 1 + int(max(width, height) / noise_thickness_para)  # 噪声宽度


def judge_coincide(image, noise):
    height, width = image.shape[:2]
    image_temp = np.ones((height, width, 3), dtype=np.uint8) * 255  # 新建一个新的空白画布
    noise.draw(image_temp, (0, 0, 0), thickness=1)
    for i in range(height):
        for j in range(width):
            temp1 = [x for x in image[i][j]]
            temp2 = [x for x in image_temp[i][j]]
            if temp1 == [0, 0, 0] and temp2 == [0, 0, 0]:
                return True
    return False


def add_noise(line_segment_lists, image):
    height, width = image.shape[:2]
    noise_thickness = get_noise_thickness(height, width)
    for _ in range(noise_number):
        noise_type = random.choices(noise_type_list, weights=noise_type_weight)[0]
        line_segment = random.choice(line_segment_lists)
        x, y = random.choice(line_segment)
        x, y = round(x), round(y)
        x_offset = random.randint(noise_x_offset_lower, noise_x_offset_upper)
        y_offset = random.randint(noise_y_offset_lower, noise_y_offset_upper)
        center = (x + x_offset, y + y_offset)
        if noise_type == 0:
            noise = Circle(center, radius=circle_radius)
            while not judge_coincide(image, noise):
                x_offset = random.randint(noise_x_offset_lower, noise_x_offset_upper)
                y_offset = random.randint(noise_y_offset_lower, noise_y_offset_upper)
                center = (x + x_offset, y + y_offset)
                noise = Circle(center, radius=circle_radius)
            noise.draw(image, (0, 0, 0), thickness=noise_thickness)
        elif noise_type == 1:
            noise = Triangle(center, length=triangle_length)
            noise.draw(image, (0, 0, 0), thickness=noise_thickness)
        elif noise_type == 2:
            noise = X(center, length=X_length)
            noise.draw(image, (0, 0, 0), thickness=noise_thickness)
        elif noise_type == 3:  # 文本图形容易偏离线段
            center = (x, y)
            text = random.choices(character_list, weights=character_weight)[0]
            noise = Character(center, text=text, font_size=font_size)
            image = noise.draw(image, (0, 0, 0))
        elif noise_type == 4:  # 数字
            center = (x + x_offset / 6, y + random.randint(5, 13))
            text = f'{random.choice([random.randint(1, 99), round(random.uniform(0, 1), 2)])}'
            noise = Character(center, text=text, font_size=font_size)
            image = noise.draw(image, (0, 0, 0))

    return image
