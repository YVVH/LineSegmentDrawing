import matplotlib.pyplot as plt
import numpy as np
import json

with open('config.json', 'r') as f:
    config = json.load(f)
l = config["l"]
h = config["h"]
n_global = config["n"]


def fun(x, n):
    return x ** (1 / n)


def inverse_fun(y, n):
    return y ** n


if __name__ == '__main__':

    # 绘图
    # 生成 x 值
    x = np.linspace(l, h, 1000)

    # 计算对应的 y 值
    y = fun(x, n_global)

    plt.figure(figsize=(8, 6))  # 设置图像大小
    plt.plot(x, y, label='y1 = f1(x)', color='blue')  # 绘制曲线
    plt.title('Function Plot')  # 设置标题
    plt.xlabel('x')  # 设置 x 轴标签
    plt.ylabel('y')  # 设置 y 轴标签
    plt.grid(True)  # 添加网格
    plt.legend()  # 显示图例
    plt.show()  # 显示图像
