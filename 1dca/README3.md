## Part 3


### The Python *interpreter* and how it runs the `DrawDots()` function


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

### Creating a real program

Now we have a picture of how the function works it is time to delete all of the test code and replace it 
with some real code that gets us closer to our goal: Watching the living space change over time. 


Go ahead and delete the test code and create a new version of livingspace. Let us make it 32 spaces across, 
all of them `False` except the middle space which will be `True`. Let us also decide that time will go forward
from zero to 19, so there will be 20 ticks on our time clock. 


Here is the code to type in: 

```
nSpaces = 32
livingspace = [False] * nSpaces
livingspace[nSpaces / 2] = True

nTimeTicks = 20
```

Notice that when we use `True` and `False` they are not in quotes. They are not text strings. They are a special
kind of variable in Python called a boolean. A boolean variable can have just about any name, just like other 
variables. For example you could be ridiculous about it: 

```
fredscatsfriendwhoisagoat = False
```

This is a perfectly fine variable name but it is not very helpful in this program. Notice it is a *boolean* with 
value `False`. You can use these in `if` statements. For example (using the above variable):


```
if fredscatsfriendwhoisagoat:
    print('How about that cat!')
else:
    print('Today is Friday')
```

What will be printed when this code runs?


Ok onward: Try running this next line of code to make sure `livingspace` is what you think it is, a list of booleans: 

```
print(livingspace)
```

Now we can create a time loop. Type this in at the bottom of your program and check that it runs properly:

```
for mytime in range(7):
    print('mytime is', mytime)
    DrawDots(livingspace, mytime)
    oldlivingspace = livingspace[:]
```

This will hopefully draw three identical versions of `livingspace` as dots, stacked vertically. What does the fourth
line of code do, the one that says `oldlivingspace = livingspace[:]`? It is mysterious... and it actually is not 
required yet; but it will be useful in what comes next. 


That line of code does a copy of the list `livingspace` into a different list called `oldlivingspace`. We need such a copy
because we are inside of a loop; and each time the clock ticks (the loop loops back around) we draw `livingspace`. In order
for `livingspace` to not be the same every time we need to change it. It will change based on what it contains... but we 
are unable to change it in place. Instead we calculate the new version of `livingspace` from its copy, `oldlivingspace`. 


Once you have the above code working add these lines of code to see how we can change `livingspace`. *Be careful!* This 
code is indented one tab so that it is *inside* the `mytime` loop. The word `for` should line up with `oldlivingspace` 
in the previous line of code. 

```
    for i in range(len(oldlivingspace)):
        if oldlivingspace[i] or oldlivingspace[i-1]: 
            livingspace[i] = True
        else:
            livingspace[i] = False
```

Now before running this program: Take a good look at it and predict what you will see. 


If it works you should see the rows changing each time. That's the end of Part 3; you are over half-way done! 
