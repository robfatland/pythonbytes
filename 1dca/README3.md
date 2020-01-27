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
livingspace = [True, False, True]
mytime = 0
DrawDots(livingspace, mytime)
# ...and so on with test code, time = 1 and time = 2
```

Notice that we have written the test code at the bottom, after the function DrawDots() is defined with `def`. 
This is necessary 
since Python runs from top to bottom. By putting `def DrawDots()` at the top the Python *kernel* knows that it
exists. The kernel is like the conductor of running the program. When we call the `DrawDots()` function in line 21 
Python's kernel knows what to do. As a narrative its thinking sounds like this: 

> Oh I must run the `DrawDots()` function. Ok: what does it expect? It expects something it will call `c` and
> another thing it will call `time` (because the `def` line reads `def DrawDots(c, time)`. Very well; what do 
> I have in the call of the function down at the bottom? I have two arguments, and they are `livingspace` and
> `mytime`. So I guess that `livingspace` is equivalent to `c` and `mytime` is equivalent to `time`. Ok I can do 
> that. Now that I know what `c` and `time` are: What else does `DrawDots()` need? Well it uses something called
> `joe`. Ah, but I see `joe` is defined even higher up in the program as a `Turtle`. So everything is covered and
> I can start running the `DrawDots()` function.

