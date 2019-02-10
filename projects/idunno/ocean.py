import numpy as np
from random import randint, uniform

np.random.seed(0)  # fixed seed for reproducibility

pixels = 640
offset = pixels / 2
ocean = np.zeros(shape=(pixels, pixels))
jump = 56
rx = 60

# print("ndim: ", ocean.ndim)
# print("shape:", ocean.shape)
# print("size: ", ocean.size)
# print("dtype: ", ocean.dtype)

# an empty ocean... 640 x 640 pixels

pollution_low = 20
pollution_high = 30
polluted = []

for x in range(0, pixels, jump):
    tx = x + randint(-rx, rx)
    ty = x + randint(-rx, rx)
    if tx < 0: tx = 0
    if tx > pixels - 1: tx = pixels - 1
    if ty < 0: ty = 0
    if ty > pixels - 1: ty = pixels - 1
    ocean[tx, ty] = float(randint(pollution_low, pollution_high))
    polluted.append((tx, ty))

# Now the ocean has some pollution

from turtle import Turtle

boat = Turtle()
boat.speed(1000)
boat.hideturtle()

pollution = Turtle()
pollution.speed(1000)
pollution.up()
pollution.hideturtle()

# pollution.colormode(1.0)

def Pollute():
    for x in range(pixels):
        for y in range(pixels):
            x1, y1 = (x + 1) % pixels, y; Ooze(x, y, x1, y1, 2.0)
            x1, y1 = (x - 1) % pixels, y; Ooze(x, y, x1, y1, .4)
            x1, y1 = x, (y + 1) % pixels; Ooze(x, y, x1, y1, 3.0)
            x1, y1 = x, (y - 1) % pixels; Ooze(x, y, x1, y1, 0.6)


def Ooze(x, y, x1, y1, threshold):
    if ocean[x, y] == 0. and ocean[x1, y1] > threshold:
        half = ocean[x1, y1]/2.
        ocean[x, y] = half
        ocean[x1, y1] = half

for time in range(30):
    print(time)
    
    # Draw the pollution
    for x in range(pixels):
        for y in range(pixels):
            if ocean[x, y] > 0. and not (x, y) in polluted:
                pollution.setpos(x - offset, y - offset)
                pollution.pencolor(uniform(0.4, 1.0),
                                   uniform(0.4, 1.0),
                                   uniform(0.4, 1.0))
                pollution.dot()
                pollution.up()
                polluted.append((x,y))

    # The pollution spreads out in some way
    Pollute()

    
    




