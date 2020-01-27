## 1dca Part 2


We need to answer two questions now. First: What is a *function*? Second: What do these six lines of code do? 

```
(1)  def DrawDots(c, time):
(2)      joe.goto(-200, 200 - 4 * time)
(3)      for i in range(len(c)):
(4)          if c[i]: 
(5)              joe.dot(2)
(6)          joe.forward(4)
```

> There is an introduction to **functions** on page 81 of your *Python for Kids* book. 

### What is a function?

In Python a function is a block of code with three parts: A *name*, some *arguments* and a *body*.
It always begins with `def` for *define*. Then the function name is **DrawDots**. There are two
arguments, `c` and `time`. The *body* of the function is the five lines of code indented below the
`def` line. 


The *name* of the function acts like a command. Who gives this command? *You* do by writing that *name* 
into other parts of your program. 


Another way to say this: 
The function is called by *name* by other lines of code, lower down in the program. 
When the function is called: The code in the *body* of the function
runs. It does stuff. In our case this function will do what the name says: It will draw some dots. 
So what are the *arguments* `c` and `time`? We get to decide that later. (This is a bit like taking 
apart a car to figure out how it works.) 


To summarize: The `DrawDots()` function will be used later in the program as a little unit of code that 
does a particular task. Functions are commonly used to bundle up code in a sensible way. They can often
be called by different parts of a program but in our case we just need to call this function once. 


### What do the lines of code in the function do?


We will come back to this later in more detail. Briefly: 


```
(1)  def DrawDots(c, time):
```
The first line of code gives the function a name
and declares two variables `c` and `time` that come into play when the body of the function runs. 

```
(2)      joe.goto(-200, 200 - 4 * time)
```
This line of code moves the turtle to the beginning of a row. Which row? The row determined by what `time` it is.

```
(3)      for i in range(len(c)):
```
This line of code creates a loop across the row. It is important to realize that `c` will be a `list` and that
`len(c)` is the *length* of that list. For this reason `range(len(c))` gives a for-loop that will scan that list `c`.

```
(4)          if c[i]: 
```
This is an `if` statement that checks whether this element of the list `c` is `True`. 

```
(5)              joe.dot(2)
```
If it *is* `True` then the turtle will draw a dot for that living space.

```
(6)          joe.forward(4)
```
Whether or not the turtle draws a dot: It must now move forward 4 pixels to the next location in this row. 


We need to test this function to make sure it works. Now that you have a sense I hope of what the function does: 
Hit Enter a couple of times in your code editor below the function and enter this test code:


```
livingspace = [True, False, True, True, False, False, True, False, False, False, True, True]
myTime = 0
DrawDots(livingspace, myTime)
```

When you run this code you should see some dots that correspond to the True / False sequence you put in `livingspace`.
Once you have this running see if you can create two more tests below the first one. You can look down below at my 
solution by scrolling down but I suggest you try it on your own first! 

```



































# second test
livingspace[1] = True
livingspace[2] = False
myTime = 1
DrawDots(livingspace, myTime)

# third test
livingspace[2] = True
livingspace[10] = False
myTime = 2
DrawDots(livingspace, myTime)
```

Make sure your code does what you expect and everything runs smoothly.

This completes Part 2; three more to go. 
