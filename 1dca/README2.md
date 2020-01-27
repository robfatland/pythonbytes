## 1dca Part 2


We need to answer two questions now. First: What is a *function*? Second: What do those lines of code do? 


> There is an introduction to **functions* on page 81 of your *Python for Kids* book. 



```
joe.dot(2) 
```

The coordinates of the turtle depend on what time it is. The time will be an integer: 0, 1, 2, 3, 4, ... 
At the start, for the first row, the time is 0. Then the time becomes 1, then 2 and so on. In my version 
of the program I set the x-coordinate always to be -200 and then I went from left to write making dots 
at each "location" where the living space list has value True. Where it is False I leave it blank. 
Each possible dot location is 4 pixels to the right of the previous one. 

```
def DrawLivingSpace(tfList, timeTick):          # tfList is a True/False list, like [True, True, False, True]
    joe.goto(-200, 200 - timeTick*4)            # this places the turtle at the left edge of the screen; the y-coordinate connects to time
    # ...and so on, need some more code here
```

Above is the start of the function. Notice that you must give it (pass the function) both your list name and what time it is. This function:

```
n = len(tfList) 
```

will set n equal to how many elements there are in the living space (True/False) list. I find this to be useful.

Finally here is an example of code testing this function:

livingSpace = [True, False, False, True, True, False, False, False, False, False, True, False, True]
DrawLivingSpace(livingSpace, 0)
livingSpace[6] = True
DrawLivingSpace(livingSpace, 1)
livingSpace[0] = False
DrawLivingSpace(livingSpace, 2)
