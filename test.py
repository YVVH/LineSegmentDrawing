import numpy as np
import cv2

from noise.noise_circle import Circle

height, width = 400, 600

image = np.ones((height, width, 3), dtype=np.uint8) * 255

noise = Circle((300, 200), radius=10)
noise.draw(image, (0, 0, 0), thickness=1)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_temp = np.ones((height, width, 3), dtype=np.uint8) * 255
cv2.line(image_temp, (0, 400), (0, 0), (0, 0, 0), 1)
cv2.imshow('image', image_temp)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_temp2 = np.ones((height, width, 3), dtype=np.uint8) * 255
cv2.line(image_temp2, (0, 400), (0, 0), (0, 0, 0), 1)
noise.draw(image_temp2, (0, 0, 0), thickness=1)
cv2.imshow('image', image_temp2)
cv2.waitKey(0)
cv2.destroyAllWindows()


def judge_coincide(image, noise):
    height, width = image.shape[:2]
    image_temp = np.ones((height, width, 3), dtype=np.uint8) * 255  # 新建一个新的空白画布
    image_temp2 = image
    noise.draw(image_temp, (0, 0, 0), thickness=1)
    for i in range(height):
        for j in range(width):
            temp1 = [x for x in image[i][j]]
            temp2 = [x for x in image_temp[i][j]]
            print(temp1, temp2)
            if temp1 == [0, 0, 0] and temp2 == [0, 0, 0]:
                return True
    return False

