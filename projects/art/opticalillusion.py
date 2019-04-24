from turtle import Turtle

square, grid = 120, 139
halfsquare = square/2
nSubSquares = 3
nHalfSubSquares = (nSubSquares - 1) / 2

t = Turtle()
t.speed(1000)
t.setpos(0,0)
t.up()

for i in range(nSubSquares):
  for j in range(nSubSquares):
    cornerX = (i-nHalfSubSquares)*grid - halfsquare
    cornerY = (j-nHalfSubSquares)*grid + halfsquare
    t.setpos(cornerX, cornerY)
    t.setheading(0)
    t.down()
    t.forward(square)
    t.right(90)
    t.forward(square)
    t.right(90)
    t.forward(square)
    t.right(90)
    t.forward(square)
    t.up()

radius = 300
ntheta = 66
dtheta = 180. / float(ntheta)

for i in range(ntheta):
  theta = float(i)*dtheta
  t.setpos(0., 0.)
  t.setheading(theta)
  t.down()
  t.forward(radius)
  t.up()
  t.setpos(0., 0.)
  t.down()
  t.forward(-radius)
  t.up()

t.hideturtle()
