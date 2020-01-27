So far we have something that looks like this:

```
from turtle import Turtle

joe = Turtle()
joe.up()
joe.pencolor("blue")
joe.speed(0)

def DrawDots(c, time):
    joe.goto(-200, 200 - time*4)
    for i in range(len(c)):
        if c[i]: 
            joe.dot(2)
        joe.forward(4)

# test code
c = [True, False, True]
time = 0
DrawDots(c, time)
# ...and so on with test code, time = 1 and time = 2
```

Notice that we have written test code at the bottom, after the function DrawDots() is defined. This is necessary 
since Python runs from top to bottom. By putting `DrawDots()` at the top the Python *interpreter* knows that it
exists. That way when we call the function in line 21 Python knows what to do. As a narrative this is: 

> Oh I must run the `DrawDots()` function. Ok: what does it expect? It expects something it will call 

