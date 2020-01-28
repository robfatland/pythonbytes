## 1dca Part 1

Create a **repl** at [**repl.it**](https://repl.it) using the **Python (with Turtle graphics)** kernel. Name it 
1dca and type this in as your first line of code: 

```
from turtle import Turtle
```

Our goal in this program is to draw (with the turtle) an interesting pattern, following a very famous recipe from
the world of computer science. The recipe is a collection of ideas that we will turn into Python code. We will use
a turtle; and some other Python items: Lists, functions, loops, and logic. I have broken this down into five parts.
This is Part 1 and it should take no more than a few minutes.


I will now give you a quick preview: That we will be drawing horizontal rows that contain both dots and spaces. 
The very first row will go from left to right across the top of the turtle's window. The turtle will draw the 
dots. The second row will be below the first, and so on down the screen. 


To get your gears turning: At this point please obtain a piece of paper and a pencil or pen. Draw a series of 16 
open circles in a row. Now pick seven of these at random and fill those ones in. It is like a street with houses; 
some empty and some occupied.


The row of circles represents sixteen "living spaces".  Becauase these are in a line, in a row, we say it is 
one-dimensional. The first row (the one you drew or the first one the program draws) represents the situation 
in the living spaces at the first moment of time. That is called time zero. We use a Python variable called time
that will start out with a value of zero. `time = 0`. 


We will use a time clock that will count upward from `time = 0`. The next time will be `time = 1` and then `time = 2`.
You can imagine this will work well as a for-loop. As time goes on our living space may change. 


As time moves along 0, 1, 2, 3, ... and the living space changes we could draw the latest picture of it over the 
previous version. However this will erase the visual information about the past. So, instead what do you imagine
we will do? Excuse me while I take a sip of my soda while you consider... 


So the idea is this: Each new version of the living space (with time) is drawn below the previous one. In this way 
time goes downwards on the paper or on the screen. Here is an example using a simple rule. Draw 16 new circles below
the first set. The rule is: If the cell is occupied it becomes empty. If it is empty it becomes occupied. You can
fill in the second row (`time = 1`) using this rule. What happens when you apply the rule again for yet another 
time step (`time = 2`)? 


As the rows accumulate from top to bottom we see time passing for the living space. 


Your next task is in the **repl.it** code. You have already begun with the line `from turtle import Turtle`. 
Now you should create a new turtle named `joe`. Set the `speed` of `joe` to be zero (that is 'fastest possible')
and set the pen to be `up`. You can also set the `pencolor` if you like; but do not change the heading of `joe`.
We want `joe` to always be facing to the right. 


Your final task in **Part 1** is to write a function. It will include six lines of code and they are all
given here. Type these lines of code beneath your other code.


```
def DrawDots(c, time):
    joe.goto(-200, 200 - 4 * time)
    for i in range(len(c)):
        if c[i]: 
            joe.dot(2)
        joe.forward(4)
```

Now run your code and check the **console** tab to make sure there are no errors. The program does not 
draw anything yet. We still need to get to the interesting part. 



