import numpy as np
import csv


# 从matplotlib坐标转为像素坐标
def get_pix_coor(line_segment, ax, fig):
    xy_pixels = ax.transData.transform(np.vstack(line_segment.coor_list))  # .T是转置
    x_pix, y_pix = xy_pixels.T
    width, height = fig.canvas.get_width_height()
    y_pix = height - y_pix

    return zip(x_pix, y_pix)


def save_csv(lists, filename, ax, fig, line_cnt):
    data = [['Line', 'Point', 'X', 'Y']] if line_cnt == 1 else []

    point_cnt = 0
    point_dict = {}  # 因为x, y四舍五入的问题，可能存在重复的点，使用字典去重
    for line_segment in lists:
        pix_list = get_pix_coor(line_segment, ax, fig)  # 从matplotlib坐标转为像素坐标
        for x, y in pix_list:
            x = round(x)
            y = round(y)
            if (x, y) in point_dict:
                continue
            point_dict[(x, y)] = 1
            point_cnt += 1
            data.append([line_cnt, point_cnt, x, y])  # 该图像只有一条线

    # 使用csv.writer写入数据到CSV文件
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入标题行
        writer.writerow(data[0])
        # 写入其余数据行
        for row in data[1:]:
            writer.writerow(row)
