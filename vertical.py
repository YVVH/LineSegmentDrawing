from LineSegment import LineSegment
import random
import matplotlib.pyplot as plt
import numpy as np
import os
from FormatTime import get_time
import csv

img_number = 30  # 图片数量
line_segment_number = 30  # 每条线线段的个数的最大值
x_axis_len = 100  # 坐标轴的范围
y_axis_len = 100  # 坐标轴的范围
img_size = (6, 4)  # 600 * 400
x_min_scale = 16  # 角度为0的时候线段长度随机取值为[0, x_axis_len / x_scale] 值越大线段长度越小
x_max_scale = 24
y_min_scale = 16  # 角度为90的时候线段长度随机取值为[0, y_axis_len / y_scale] 值越大线段长度越小
y_max_scale = 24
slash_scale = 2  # 画斜线时长度扩大
slash_prob = 0.1  # 斜线在随机时的概率

img_dpi = 100  # 图像dpi值，目前无意义

# 起点x轴偏移量
x_axis_offset_lower = 5
x_axis_offset_upper = 15
# 起点y轴偏移量
y_axis_offset_lower = 5
y_axis_offset_upper = 15

x_lower = x_axis_len / x_max_scale
x_upper = x_axis_len / x_min_scale
y_lower = y_axis_len / y_max_scale
y_upper = y_axis_len / y_min_scale

# 图像计数
filename_cnt = 1

# 创建目录
origin_path = 'output/'
img_folder_path = origin_path + 'img/' + get_time() + '/'
corr_folder_path = origin_path + 'corr/' + get_time() + '/'


def make_dir(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        # 如果不存在，创建文件夹
        os.mkdir(folder_path)


def plot(line_segment):
    x1, y1 = line_segment.point1
    x2, y2 = line_segment.point2
    ax.plot((x1, x2), (y1, y2), '-', color='black', linewidth=1)


def get_random_normal(lower, higher):
    # 设置正态分布的参数
    mean = (lower + higher) / 2  # 平均值设置为区间的中点
    stddev = (higher - lower) / 4  # 标准差，越大越分散

    # 生成一个在指定区间内符合正态分布的随机数
    random_number = np.random.normal(mean, stddev)

    # 确保生成的随机数在指定的区间内
    if random_number < lower:
        random_number = lower
    elif random_number > higher:
        random_number = higher

    return random_number


def save_img():
    filename = img_folder_path + f"{filename_cnt:03d}.png"

    # 隐藏坐标轴
    ax.set_frame_on(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # plt.show()

    # 保存图像为PNG格式
    plt.savefig(filename, format='png')

    # 清空画布内容
    plt.close()


def save_csv(lists):
    filename = corr_folder_path + f"{filename_cnt:03d}.csv"
    data = [
        ['Line', 'Point', 'X', 'Y'],
    ]

    point_cnt = 0
    for line_segment in lists:
        pix_list = get_pix_coor(line_segment)
        for x, y in pix_list:
            # print(cnt, (x, y))
            point_cnt += 1
            x = round(x)
            y = round(y)
            data.append([1, point_cnt, x, y])  # 该图像只有一条线

    # print(data)

    # 使用csv.writer写入数据到CSV文件
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入标题行
        writer.writerow(data[0])
        # 写入其余数据行
        for row in data[1:]:
            writer.writerow(row)


# 从matplotlib坐标转为像素坐标
def get_pix_coor(line_segment):
    xy_pixels = ax.transData.transform(np.vstack(line_segment.coor_list))  # .T是转置
    x_pix, y_pix = xy_pixels.T
    width, height = fig.canvas.get_width_height()
    y_pix = height - y_pix

    return zip(x_pix, y_pix)


if __name__ == '__main__':
    make_dir(img_folder_path)
    make_dir(corr_folder_path)
    for i in range(img_number):
        # 创建一个新的图形和轴
        fig, ax = plt.subplots()
        fig.set_size_inches(img_size)
        # 设置坐标轴的范围
        ax.axis([-1, x_axis_len + 1, -1, y_axis_len + 1])
        # 存储所有线段，便于以后保存坐标
        line_segment_lists = []

        # 起点
        x_axis_offset = random.uniform(x_axis_offset_lower, x_axis_offset_upper)
        y_axis_offset = random.uniform(y_axis_offset_lower, y_axis_offset_upper)
        point = (x_axis_offset, y_axis_offset)

        last_choice = -1

        angle_list = [0, 90, -1]  # 可选角度
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
                length_x = random.uniform(x_lower, x_upper * slash_scale)
                length_y = random.uniform(y_lower, y_upper * slash_scale)

                if length_x + point[0] > x_axis_len:
                    length_x = x_axis_len - point[0]
                if length_y + point[1] > y_axis_len:
                    length_y = y_axis_len - point[1]

                angle_list = [0, 90]
                angle_weight = [0.5, 0.5]
                if length_x == 0 and length_y == 0:
                    break  # 无意义的画线
                line = LineSegment(point, (length_x + point[0], length_y + point[1]))

            # # 正态分布：
            # if angle == 0:
            #     length = get_random_normal(1, x_axis_len / x_min_scale)
            #     if length + point[0] > x_axis_len:
            #         length = x_axis_len - point[0]
            # else:
            #     length = get_random_normal(1, y_axis_len / y_min_scale)
            #     if length + point[1] > y_axis_len:
            #         length = y_axis_len - point[1]

            plot(line)
            point = line.point2
            line_segment_lists.append(line)
        save_csv(line_segment_lists)
        save_img()
        print(f'已经生成{filename_cnt}张图片')
        filename_cnt += 1
