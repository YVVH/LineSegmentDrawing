import cv2
from LineSegment import LineSegment
import random
import numpy as np
import os
from FormatTime import get_time
from CoordinateSave import save_csv

img_number = 30  # 图片数量
line_segment_number = 30  # 每条线线段的个数的最大值
img_size = (600, 400)  # 600 * 400
width, height = img_size
line_thickness_para = 1000  # 线段宽度，像素值每增大1000线段宽度+1
# 角度为90的时候线段长度随机取值为[0, y_axis_len / y_scale] 值越大线段长度越小
# 角度为0的时候线段长度随机取值为[0, x_axis_len / x_scale] 值越大线段长度越小
x_min_scale, x_max_scale, y_min_scale, y_max_scale = 12, 30, 12, 30
slash_min_scale, slash_max_scale = 1, 2  # 画斜线时的长度系数的随机范围
slash_prob = 0.02  # 随机到画斜线的概率
x_lower_ratio, x_upper_ratio, y_lower_ratio, y_upper_ratio = 0.05, 0.15, 0.05, 0.15  # 子图边缘与其所在轴的边缘之间的距离比例的取值范围

thickness = 1 + int(max(width, height) / line_thickness_para)  # 线段宽度

# 图像计数
filename_cnt = 1

# 创建目录
origin_path = 'output/'
img_folder_path = origin_path + 'img/' + get_time() + '/'
corr_folder_path = origin_path + 'corr/' + get_time() + '/'


def axis_convert(y):
    return height - y


def make_dir(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        # 如果不存在，创建文件夹
        os.mkdir(folder_path)


def plot(line_segment):
    x1, y1 = line_segment.point1
    x2, y2 = line_segment.point2
    x1, y1 = round(x1), round(y1)
    x2, y2 = round(x2), round(y2)
    cv2.line(image, (x1, axis_convert(y1)), (x2, axis_convert(y2)), (0, 0, 0), thickness=thickness)


def save_img():
    filename = img_folder_path + f"{filename_cnt:03d}.png"

    cv2.imwrite(filename, image)


if __name__ == '__main__':
    make_dir(img_folder_path)
    make_dir(corr_folder_path)
    for i in range(img_number):
        # 创建一个新的图形
        image = np.ones((height, width, 3), dtype=np.uint8) * 255
        # 存储所有线段，便于以后保存坐标
        line_segment_lists = []

        # 子图边缘与其所在轴的边缘之间的距离比例
        left_ratio = random.uniform(x_lower_ratio, x_upper_ratio)
        right_ratio = random.uniform(x_lower_ratio, x_upper_ratio)
        bottom_ratio = random.uniform(y_lower_ratio, y_upper_ratio)
        top_ratio = random.uniform(y_lower_ratio, y_upper_ratio)

        x_axis_margin = width * left_ratio
        y_axis_margin = height * bottom_ratio

        # 右侧和上侧留白
        x_axis_len = width - width * right_ratio
        y_axis_len = height - height * top_ratio

        # 原点
        point = (x_axis_margin, y_axis_margin)

        # 每次随机的线段长度的取值范围
        x_lower = x_axis_len / x_max_scale
        x_upper = x_axis_len / x_min_scale
        y_lower = y_axis_len / y_max_scale
        y_upper = y_axis_len / y_min_scale

        last_choice = -1

        angle_list = [0, 90, -1]  # 可选角度 -1为斜线
        angle_weight = [(1 - slash_prob) / 2, (1 - slash_prob) / 2, slash_prob]  # 随机权重

        for _ in range(line_segment_number):
            angle = random.choices(angle_list, weights=angle_weight)[0]

            if angle == 0 or angle == 90:  # 画水平竖直线的情况
                # 均匀分布：
                if angle == 0:
                    length = random.uniform(x_axis_len / x_max_scale, x_axis_len / x_min_scale)
                    if length + point[0] > x_axis_len:  # 超过x_axis_len的部分不画
                        length = x_axis_len - point[0]
                else:
                    length = random.uniform(y_axis_len / y_max_scale, y_axis_len / y_min_scale)
                    if length + point[1] > y_axis_len:
                        length = y_axis_len - point[1]

                angle_list = [0, 90, -1]  # 可选角度
                angle_weight = [(1 - slash_prob) / 2, (1 - slash_prob) / 2, slash_prob]  # 随机权重

                if length == 0:
                    break
                line = LineSegment(point, length, angle)
            else:  # 画斜线的情况
                length_x = random.uniform(x_lower, x_upper * random.uniform(slash_min_scale, slash_max_scale))
                length_y = random.uniform(y_lower, y_upper * random.uniform(slash_min_scale, slash_max_scale))

                if length_x + point[0] > x_axis_len:
                    length_x = x_axis_len - point[0]
                if length_y + point[1] > y_axis_len:
                    length_y = y_axis_len - point[1]

                angle_list = [0, 90]
                angle_weight = [0.5, 0.5]
                if length_x == 0 and length_y == 0:
                    break  # 无意义的画线
                line = LineSegment(point, (length_x + point[0], length_y + point[1]))

            plot(line)
            point = line.point2
            line_segment_lists.append(line)
        filename = corr_folder_path + f"{filename_cnt:03d}.csv"
        save_csv(line_segment_lists, filename, 1, axis_convert)
        save_img()
        print(f'已经生成{filename_cnt}张图片')
        filename_cnt += 1
