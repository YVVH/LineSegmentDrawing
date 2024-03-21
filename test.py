import matplotlib.pyplot as plt

from LineSegment import LineSegment

img_size = (6, 4)

fig, ax = plt.subplots()

ax.axis([-1, 101, -1, 101])

line = LineSegment((0, 0), 100, 0)

points, = ax.plot((-100, 100), (-100, 100), '-')

plt.show()