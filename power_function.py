import math
import matplotlib.pyplot as plt
import numpy as np
import json

with open('config.json', 'r') as f:
    config = json.load(f)
l = config["l"]
h = config["h"]
k = config["k"]


def fun(x, n):
    if x > 0:
        return x ** (1 / n)
    else:
        return (-x) ** (1 / n)


def inverse_fun(y, n):
    if y > 0:
        return y ** n
    else:
        return (-y) ** n


if __name__ == '__main__':
    n_it = 0.01
    while 1:
        x1 = fun(l, n_it)
        x2 = fun(h, n_it)
        x3 = fun((l + h) / 2, n_it)

        if math.fabs((x3 - x1) / (x2 - x3) - k) < 0.01:
            break
        n_it += 0.01

    config["n"] = n_it

    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)

    # # 绘图
    # # 生成 x 值
    # x = np.linspace(l, h, 1000)
    #
    # # 计算对应的 y 值
    # y = fun(x, n_it)
    #
    # plt.figure(figsize=(8, 6))  # 设置图像大小
    # plt.plot(x, y, label='y1 = f1(x)', color='blue')  # 绘制曲线
    # plt.title('Function Plot')  # 设置标题
    # plt.xlabel('x')  # 设置 x 轴标签
    # plt.ylabel('y')  # 设置 y 轴标签
    # plt.grid(True)  # 添加网格
    # plt.legend()  # 显示图例
    # plt.show()  # 显示图像
