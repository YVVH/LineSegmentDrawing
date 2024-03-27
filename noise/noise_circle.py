import cv2


class Circle:
    def __init__(self, center, radius):
        """
        初始化一个圆形对象。

        :param center: 圆心的坐标，以(x, y)的形式表示。
        :param radius: 圆的半径。
        :param color: 圆的颜色，以BGR格式表示。
        :param thickness: 圆的线条粗细，如果是负值表示填充圆。
        """
        self.center = center
        self.radius = radius
        self.image = None  # 用于存储绘制圆后的图像

    def draw(self, image, color, thickness=1):
        """
        在给定的图像上绘制圆。
        :param image: 要绘制圆的图像。
        """
        cv2.circle(image, self.center, self.radius, color, thickness)
        # 绘制圆心的点
        cv2.circle(image, self.center, 1, color, -1)

