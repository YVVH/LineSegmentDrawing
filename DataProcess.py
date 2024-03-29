"""
给原有数据添加噪声
"""
from AddNoise import add_noise
import cv2
import csv
import os

filename_cnt = 1


def get_location():
    return str(os.listdir('output/corr')[-1])


# 读取数据
# 获取文件信息
def process_csv(csv_file_path):
    coor_lists = []
    coor_list = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csv_file = csv.reader(csvfile)
        now = 1
        for row in csv_file:
            if row[0] == 'Line':
                continue
            if str(now) != row[0]:
                coor_lists.append(coor_list)
                now += 1
                coor_list = []
            coor_list.append([int(row[2]), int(row[3])])
        coor_lists.append(coor_list)
    return coor_lists


if __name__ == '__main__':
    folder_path = get_location()
    csv_path = 'output/corr/' + folder_path
    img_path = 'output/img/' + folder_path
    # 读取坐标信息
    for root, dirs, files in os.walk(csv_path):
        for file in files:
            if file.endswith('.csv'):
                csv_file_path = csv_path + '/' + file
                img_file_path = img_path + '/' + file[0:-4] + '.png'
                coor_lists = process_csv(csv_file_path)
                image = cv2.imread(img_file_path)
                height, width = image.shape[:2]
                image = add_noise(coor_lists, image)
                cv2.imwrite(img_file_path, image)  # 保存图片
