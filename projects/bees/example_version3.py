import requests
import pygame

drones_lost = 0


# This talks to the Internet to find out how many bees are at (x, y, z) ... or 'drone_lost' 
def Bees(x, y, z):
    return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?' + \
        'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# This creates a little text map of how many bees were found at a grid of locations
def MapBees(x0, y0, z0, r, n):
    global drones_lost
    thisZ = float(z0)
    xa = float(x0 - r)
    xb = float(x0 + r + n)
    dx = 2*r/n
    ya = float(y0 - r)
    yb = float(y0 + r)
    dy = int(2*r/n)
    for i in range(int(n + 1)):
        thisRow = ''
        thisX = xa + i * dx
        for j in range(int(n + 1)):
            thisY = ya + j * dy
            while True:
                b = Bees(thisX,thisY,thisZ)
                if b == 'drone lost': drones_lost = drones_lost + 1
                else: break
            if j == 0: thisRow = str(round(thisX, 1)) + ':  ' + str(round(thisY, 1)) + ' ' + b
            else: thisRow += '   ' + ' ' + str(round(thisY, 1)) + ' ' + b
        print(thisRow)
        print()


# This asks for a new center location (including z) and a radius and a spacing parameter
#   and it goes out and does a square grid of bee counts. It keeps iterating so you can
#   use your evaluation of the data to configure your next search.
def InteractiveLoop():
    while True:
        x0 = float(input('x0: '))
        y0 = float(input('y0: '))
        z0 = float(input('z: '))
        radius = float(input('radius: '))
        n = float(input('n intervals: '))
        dd = drones_lost
        MapBees(x0, y0, z0, radius, n)
        print('\n', drones_lost, ' drones lost total; ', drones_lost - dd, ' this go-round')
        answer = input('quit? ')
        if answer == 'y' or answer == 'yes': break

# This actually starts things off
InteractiveLoop()
