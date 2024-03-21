import numpy as np
import matplotlib.pyplot as plt

from LineSegment import LineSegment

img_size = (6, 4)

fig, ax = plt.subplots()
points, = ax.plot((0, 100), (50, 50), '-')
ax.axis([-1, 101, -1, 101])
line = LineSegment((0, 0), 100, 0)
# Get the x and y data and transform it into pixel coordinates
print(np.vstack(line.coor_list).T)
xy_pixels = ax.transData.transform(np.vstack(line.coor_list).T)
xpix, ypix = xy_pixels.T

# In matplotlib, 0,0 is the lower left corner, whereas it's usually the upper
# left for most image software, so we'll flip the y-coords...
fig.set_size_inches(img_size)
width, height = fig.canvas.get_width_height()
print(width, height)
ypix = height - ypix

print('Coordinates of the points in pixel coordinates...')
for xp, yp in zip(xpix, ypix):
    print('{x:0.2f}\t{y:0.2f}'.format(x=xp, y=yp))

plt.show()