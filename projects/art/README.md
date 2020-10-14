# PythonBytes Project In-Depth


## Art


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/art#pythonbytes-project-in-depth)


### Overview


Interested in art and design via computer?  What sort of art might you create? One approach is to look for inspiration in the 
paintings of the 20th and 21st century. You might for example use a search engine to find sources of **abstract art**. 
I found Piet Mondrian...


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/mondrian.png" alt="drawing" width="350"/>


and  


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/abstract.png" alt="drawing" width="400"/>


Optical illusions can be artistic... 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/opticalillusion.png" alt="o-illusion" width="400"/>


Could you write a Python program to produce something like this?


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/lines.png" alt="drawing" width="300"/>


The
[Stargirl project](https://github.com/robfatland/pythonbytes/tree/master/projects/stargirl#pythonbytes-project-in-depth)
produced this image...

<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/stargirl/trajectories.png" alt="drawing" width="400"/>


The 
[fractals-I](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-I#pythonbytes-project-in-depth)
and 
[fractals-II](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-II#pythonbytes-project-in-depth)
projects will also produce some interesting images for you to enjoy.


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/julia.png" alt="drawing" width="300"/>


### Spoiler Alert!

If you want to continue under your own power: Don't read any further; the next section has *spoilers* on how to
approach the Piet Mondrian painting (the first one up at the top). What is not a spoiler is to mention to you that
there is a [reference website for turtle graphics here](https://docs.python.org/3.3/library/turtle.html) that can
be very helpful!


### Details with spoilers


Let's take a moment to start the Mondrian painting shown at the top of this page. Our background might be beige 
or something (it is at cswonders) so let's begin by drawing a large white rectangle. This will be our painting canvas. 
I also put a red rectangle on top of that...


```
from turtle import Turtle

artist = Turtle()
artist.hideturtle()
artist.speed(1000)

def rectangle(t, llh, width, height, color):
    t.up(); 
    t.pencolor(color); 
    t.fillcolor(color); 
    t.setpos(llh); 
    t.down()
    t.begin_fill()
    t.setheading(0); 
    t.forward(width); 
    t.setheading(90); 
    t.forward(height)
    t.setheading(180); 
    t.forward(width); 
    t.setheading(270); 
    t.forward(height)
    t.end_fill(); t.up()

rectangle(artist, (-200,-200), 400, 400, 'white')

rectangle(artist, (-200, 194), 185, 6, 'red')

print('...voila!...')
```

Notice that the code above uses a function called `rectangle()` which is a sequence of turtle graphics methods: up() and 
begin_fill() and so on. I have separated commands by semi-colons to make it a little easier to read. The idea is for 
every one of those commands to make sense to you. What is the purpose of `t.up()`? Of `t.begin_fill()` and `t.end_fill()`?


Another question: If the turtle is called `artist` then why does the `rectangle()` function use `t.up()` and not
`artist.up()`? 


Working from this starting point you should be able to put
together a pretty good approximation of Piet Mondrian's painting. And we're off and running!


