import csv


def save_csv(lists, filename, line_cnt, axis_convert):
    data = [['Line', 'Point', 'X', 'Y']] if line_cnt == 1 else []

    point_cnt = 0
    point_dict = {}  # 因为x, y四舍五入的问题，可能存在重复的点，使用字典去重
    for line_segment in lists:
        pix_list = line_segment.coor_list
        for x, y in pix_list:
            x = round(x)
            y = round(axis_convert(y))
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
