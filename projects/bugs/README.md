# PythonBytes Project In-Depth

## Four Bugs


### Select the Python + Turtle environment at [repl.it](http://repl.it)


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/bugs#pythonbytes-project-in-depth)


### Overview

Four bugs -- call them A, B, C, and D -- are at the corners of a square table of side *s*. Each bug
faces the bug at the next corner to their left: A faces B, B faces C, C faces D and D faces A. At a 
signal all the bugs begin walking: Each towards the bug it is facing. They take identical-length tiny bug steps
and as you might imagine they constantly adjust the direction of their walk. For example A starts walking towards
B but as B is walking towards C: A will have to adjust her path to the right to keep walking directly towards B. 


Eventually all of the bugs meet at the center of the table. When they do: How far has each walked? 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/bugs/bugpaths2.png" alt="drawing" width="400"/>


#### An unhelpful and confusing paragraph...


Now you are probably wondering what the bugs' real names are. I was too until I looked it up. They are named Alpher, 
Bethe, Gamow and Dyson. You would think that bug C would be called Camow but nope! It is Gamow. You can look up Alpher 
Bethe and Gamow on Wikipedia but it will not mention Dyson. He came along later to explain everything. 


### Now what?

* We suggest you work on this project at [repl.it](http://repl.it) using their **Python + Turtle** environment
* If you work on this at cswonders on Code Pad: Copy and paste your code into OneNote so you don't lose it
* For useful tips see **Details** below, particularly on turtle graphics
* Be sure to sign up for this project with the coaches
* Be sure to ask for help if you happen to get stuck
* **SPOILER ALERT** There are example programs in this folder that you can look at...


### Details


The technical word for one thing chasing after another is 'pursuit'. Often the paths of pursuit are pretty 
and/or interesting curves. Pursuit problems in Python can make good use of turtle graphics. Why? Because turtle 
graphics has built in *methods* to keep the bugs moving in the right direction. 
This section explains the key ones you can use.


Suppose we have a turtle called **a** and another called **b**:


```
from turtle import Turtle

a = Turtle()
b = Turtle()
```

Sometimes I call **a** and **b** turtles... and sometimes I call them bugs. 

Now we can set their pen colors and their positions:

```
a.pencolor('red')
b.pencolor('green')
a.setpos(200, 200)
b.setpos(200, -200)
```

Our drawing canvas might be 400 x 400 pixels with coordinates going from -200 to 200, both `x` and `y`. 
Now as our turtles move we can observe their progress.


#### Pursuit


On the table-top there is an angle from turtle **a** to turtle **b**. We can determine this angle
using `towards()`...


```
angle_a_to_b = a.towards(b)
```

Notice that angle_a_to_b is a variable and its value will be -90.0 at the start: angles are measured in degrees. 
What would be the angle if we did ```b.towards(a)```? I'll give you a moment to consider and give the answer below.
The key is that the positive x axis is at angle zero degrees relative to the origin.


Now that we know the angle from a to b: How do we point turtle **a** towards turtle **b**?
(Or point bug **a** towards bug **b** if you like.) We use `setheading()`. 
By the way the answer to the above question is +90.0 degrees. 


```
a.setheading(angle_a_to_b)
```

Now bug **a** is facing towards bug **b**: We used `angle_a_to_b` to set the direction of **a** to face **b**. 
We can tell bug **a** to take a tiny step forward using 'forward()`. 


```
tiny_step = 0.05
a.forward(tiny_step)
```


Now **a** has moved a little bit closer to **b**. Pursuit!


The trick of the program of course is to have all four bugs taking these little tiny steps at the same time. 
You do not want one of the bugs taking more steps than the others at this point.


#### Arriving at the center of the table


How do we know that all of the bugs have come together at the center of the table? 
We use the turtle graphics method `distance()`...


distance_a_to_b = a.distance(b)


At the start (see above) this distance would be 400.0. This is the length
of the edge of the table **s**. When the bugs are very close together the
distance will be close to zero; maybe one and a half tiny bug steps.
Checking this distance will let you choose when the bugs can stop walking.


Then it remains to report how far each one has walked... so do keep track of that! 


### Making the problem more complicated


This problem can be extended in a few different ways...


#### How many diagonal crossings?


This is more of a thinking problem than a Python problem. 


* Suppose two diagonals are drawn between opposite corners across the square table
* Does a bug starting at one corner ever cross the next diagonal on its walk? 
* Does it cross more than one diagonal?
* How many diagonals does it cross before it reaches the center?


#### Different shapes for the table


* Our table was square... what happens if it is a triangle (3 bugs)? A hexagon (6 bugs)? A tightrope? (2 bugs)
* What is the distance the bugs walk for a regular polygon with **n** sides each of length **s**?
  * This is a challenging math problem


#### Random bugs

* Choose **n** to be your number of bugs in order: **a**, **b**, **c**, **...**, **n**
  * **n** might be 3 or it might be 50 or whatever...
* Place the **n** bugs on a large table in order...
  * Place them in random locations...
  * Each bug is facing the next bug and the last bug **n** is facing the first **a**
  * Some bugs will be closer to their pursuer than others
* Version 1: All bugs go at the same speed. What happens?
* Version 2: Bug speed is proportional to their distance to the bug they are chasing
  * The farther away the bug is the faster they walk

What happens? 

Can you invent any other versions of **bugs** that are interesting to think about?



