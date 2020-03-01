# Pygame


Pygame is a pleasant Python library for making graphical games. As always there is no substituting for creativity 
and hard work! But figuring out Pygame will help you put your beautiful ideas together in a working program. 


We take as our start a program called `ball`. It seems that infinite loops are part of some Pygame programs
to "keep the action going" and this program is no exception. It contains a `while` loop that is interrupted
only when a person presses a key on the keyboard.

In order for this program to work you will need a file called `ball.png` in the same location as your code. It
should be a small image of a ball, assumed here to be a soccer ball of some sort.


## `ball` code

```
####################################
#
#          UPPER part
#

import pygame, time, sys
from random import randint   # not used here... but available for experiments

pygame.init()
pygame.display.set_caption("ball: a simple pygame program")
width = 780
height = 560
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)
blue = (0, 0, 255)  
green = (0, 255, 0)   

# This code is commented out. What would it do?
# screen.fill(green)
# pygame.draw.line(screen, white, (200, 20), (300, 170), 5)
# pygame.draw.line(screen, blue, (280, 90), (400, 130), 25)
# pygame.display.flip()

screen.fill(green)
done = False
xSpeed = 1
ySpeed = 1
ballSpeed = [xSpeed, ySpeed]
ball = pygame.image.load("ball.png")
ballRectangle = ball.get_rect()

####################################
#
#          WHILE part
#

# Notice this is a forever-while loop unless the variable done is set to True...
while not done:

  # Check the event list (things the User has done) for a key press
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
      done = True
      
  # Refresh the screen background
  screen.fill(green)
  
  # What is "blit"?
  screen.blit(ball, ballRectangle)
  
  # Move the ball according to 'ballSpeed' which is both how fast and direction
  ballRectangle = ballRectangle.move(ballSpeed)
  
  # What do these two lines do?
  if ballRectangle.left < 0 or ballRectangle.right > width: ballSpeed[0] = -ballSpeed[0]
  if ballRectangle.top < 0 or ballRectangle.bottom > height: ballSpeed[1] = -ballSpeed[1]
  
  time.sleep(.01)
  pygame.display.flip()


```
#### Student requests some help. 


I could use some help. This program is very complicated and hard to understand. 


#### Teacher reply 


Ok let's spend some time going through the program.

The program has two sections: The section above the while loop (`while not done:`) and the section of code *in* the 
while loop. Let's call these the **UPPER** and the **WHILE** sections of the program, ok?


In your program you have a variable `ball` that is assigned the image of the ball in the UPPER part. 
`ball = pygame.image.load("ball.png")` reads from an image and places some pixels that look like a 
soccer ball in the `ball` variable. 


Now `ball` is not just "some pixels". It is an example of something "that you can draw on" 
in Pygame and this is called a *surface*. So `ball` is a pygame surface and so is the `screen` that you 
display. In order to see the ball on the screen we will need to draw the `ball` surface on the `screen` 
surface. So we need to tell the program where to do this drawing. We will get to all of this below; 
just for now notice that `ball` is a surface that is covered with pixels that make it look like 
a soccer ball.


PyGame is not good at moving a surface like `ball`. Pygame is good at drawing something like `ball`
at some *location* which we can store in a different sort of object called a `Rect`.
`Rect` is short for rectangle. So on the very next line of the UPPER code we use 
`ball` to create a `Rect` (rectangle) called `ballRectangle`. 


What we do later on is move `ballRectangle` around and use its position to tell 
pygame where to draw the `ball` surface on the `screen` surface. 


When we move the Rect `ballRectangle` we use a short list of just two numbers to change its 
location. The first number in this short list is how far the rectangle moves left/right (x-coordinate) 
and the second number is how far the rectangle moves up/down (y-coordinate).


Ok with this in mind let's look how this list is created, also in the UPPER code. We have `xSpeed = 1` and 
`ySpeed = 1`; and then we make the little list `ballSpeed = [xSpeed, ySpeed]`. Now when we move the rectangle 
its coordinates will change by `+1` and `+1` so it will move one pixel to the right and one pixel down. If we made 
`ySpeed = -1` then the rect would move up instead of down. 


Now let's move to the WHILE section of the program. 


At the top of this section it has the line `while not done:` and this translates to 
"keep doing this code inside the while loop forever". There are two tricky things 
about this `while` statement. The first is that `done` is actually a variable that is 
set to `False`. So if we had written `while done:` the while loop would never do anything. 
You can test this by getting rid of the `not`. Since `done = False` the while statement is 
saying `while False` and a while loop only runs if it evaluates what comes after the word 
while as `True`. This is like saying `while you are seventeen feet tall: Eat your vegetables.` 
You never have to eat your vegetables because you are not seventeen feet tall.


But of course we know that the while loop does run and keep running. Why? I'm sure you have guessed 
it is because of the word `not`. Now it becomes `while you are not seventeen feet tall: Eat your vegetables.` 
This time you have to eat your vegetables forever because the word `not` flips the logic from `False` to `True`. 
That is: `not False` is the same as `True`.


So far so good: Now we know that we are using the `ball` surface and the `ballRectangle` Rect inside a 
while loop that runs forever. And `ballRectangle` keeps track of where the ball is. 


Inside this while 
loop there are six little blocks of code so let's figure out what they do in order.


The first bit of code checks to see if you pushed one of the keys on the keyboard. 
If you did it changes the value of  `done` to `True` so now the program will quit the while loop. 
(How does the `not` play into this?) You might want to test this feature by running the program 
and pressing a key.


This leaves us with five blocks of code to figure out.


The next block of code is easy: It just repaints the entire Pygame `screen` green. That will wipe out 
any pictures of balls that might be on the display.


Next, in the third bit of code we have the mysterious line `screen.blit(ball, ballRectangle)`. 
The word `blit` means `draw a surface on me`. That is: The screen is saying ***draw the `ball` surface
on me, the `screen` surface, and do that at the location given by the rectangle `ballRectangle`***. 


So we have an example of a function (or method) `blit()` that belongs to the object `screen`. 


The function `blit()` expects two pieces of information: Fist the name of the surface to draw on itself 
(which remember is `ball`) and second `blit()` needs the location to draw that surface. We provide
this location via the `Rect` 
`ballRectangle`. So there: That mysterious line of code drew a new soccer ball on our nice 
clean green screen just where `ballRectangle` said.


The next line of code moves the rectangle `ballRectangle` to a new location using `ballSpeed`.


The next two lines of code flip the ball speed either horizontally or vertically if the `ball` 
has reached the edge of the `screen`. This keeps the `ball` bouncing around inside the `screen` 
and not wandering off where we can't see it.


Finally in the last bit of code the program does two things. It goes to sleep for a bit 
so that the ball does not move too fast. See what happens when you comment out this line 
of code. And then finally the program does a `flip()` which updates the display. We do this 
so we actually see the results of everything we did to the `screen` surface. It is connected
to the display, the thing we actually see.


Ok I hope this helps. You are right: There is a lot here to figure out.


#### Student reply

Your explanation helps. I made the ball go faster and it wasn't hard since I barely had to change any code.

#### Teacher reply

Fantastic. What happens if you comment out the sleep(0.01) for the ball?


Here is one more idea for you to try out: I wonder if you could animate three 
different pictures at the same time. They could be three balls or one ball and 
one pig and one rock.
