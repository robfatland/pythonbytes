# PythonBytes Project In-Depth


## Art


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/art#pythonbytes-project-in-depth)


### Overview


A number of Python Bytes students expressed an interest in art and design via computer. Often artists use special
creative Apps but here we are learning to program in Python; so you are the person creating (and using) the App. 


What sort of art might you create? One approach is to look for inspiration in the paintings of the 20th and 21st
century. You might for example use a search engine to find sources of **abstract art**. I found Piet Mondrian...


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/mondrian.png" alt="drawing" width="350"/>


and here is another but who was the artist? 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/abstract.png" alt="drawing" width="400"/>


Could you write a Python program to produce something like this?


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/lines.png" alt="drawing" width="300"/>


What about other Python Bytes projects? Take a look at the 
[Stargirl project page](https://github.com/robfatland/pythonbytes/tree/master/projects/stargirl#pythonbytes-project-in-depth)
that produces this image...

<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/stargirl/trajectories.png" alt="drawing" width="400"/>


The 
[fractals-I](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-I#pythonbytes-project-in-depth)
and 
[fractals-II](https://github.com/robfatland/pythonbytes/tree/master/projects/fractals-II#pythonbytes-project-in-depth)
projects will also produce some interesting images for you to enjoy.


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/art/julia.png" alt="drawing" width="300"/>


### Details


Let's take a moment to start the Mondrian painting shown at the top of this page. Our background might be beige 
or something (it is at cswonders) so let's begin by drawing a large white rectangle. This will be our painting canvas. 


```
from turtle import Turtle

artist = Turtle()
artist.hideturtle()
artist.speed(1000)

def rectangle(t, llh, width, height, color):
    t.up(); t.pencolor(color); t.fillcolor(color); t.setpos(llh); t.down()
    t.begin_fill()
    t.setheading(0); t.forward(width); t.setheading(90); t.forward(height)
    t.setheading(180); t.forward(width); t.setheading(270); t.forward(height)
    t.end_fill(); t.up()

rectangle(artist, (-200,-200), 400, 400, 'white')

print('...voila!...')
```


