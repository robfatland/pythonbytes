## 1dca lesson Part 5

### Before we get started

The code for this program may seem mysterious or a bit complicated. This is why I broke the project down into five 
parts, to try and make it a more gradual hill to climb. My goal is to show you what is possible with just
a few lines of code without staying in the area of super-basic. There are two good results of this approach; 
at least I hope. First this code is from real computer science. It is an open door into a world of ideas 
that stretch our imagination and make new discoveries possible; which is fun. 


Second: My hope is that by seeing certain patterns in the Python code -- the way it is written -- you will
begin to see the elegance of computer programming. If you listen to an unfamiliar language being spoken 
it might not make sense at first but it certainly can sound very beautiful; so then there is the opportunity
to learn that language and make those wonderful sounds as well. 


So before going any further: Thank you for giving this a try! I appreciate your adventurous spirit. 


### What did that rule do? 


Remember that our rule was written as a list of boolean values `True` and `False`: 

```
    rule = [False, True, False, True, True, False, True, False]
````

These have eight indices: 0, 1, 2, 3, 4, 5, 6 and 7. So `rule[6]` has value `True`and 
`rule[7]` has value `False`. 
If we say `print(rule[2])` we should see **True**. So now here is the key idea: 


***The eight rule values provide us all possible new values for a cell in `livingspace`.***


Ok what does this mean? Why *eight* values and not nine? What does *possible* mean? 


Let's work from an example. We will focus on cell number 7: What happens there at the next
time tick? Cell number 7 is going to have a new value based on what is found
in cell 6, in cell 7 and in cell 8. That is, in cell 7 and in its two neighbors. Let's describe every 
possibility for these cells, supposing we do not know what they actually are. 
I use `o` for a cell that is occupied and `-` for a cell that is empty. 

```
cell location  6   7   8
               -   -   -        all three cells are empty
               -   -   o        cell 8 is occupied, 6 and 7 are empty
               -   o   -        only cell 7 is occupied
               -   o   o        ...and...
               o   -   -        ...so...
               o   -   o        ...on...
               o   o   -        ...until we reach...
               o   o   o        all three cells are occupied
```

Now let us examine the numbers 0, 1, 2, 3, 4, 5, 6 and 7 if they are written in base-2 (binary) notation.


```
decimal            binary (requires three digits: 4s, 2s and 1s)
   0                000  
   1                001 
   2                010
   3                011
   4                100
   5                101
   6                110
   7                111
```

If we compare these two listings -- the possiblities for cells 6, 7 and 8 and the 
binary values -- we notice they match up
perfectly. This means that we can use cells 6, 7 and 8
as a three-digit binary number. That is: There are 8 possibilities for cells 
6, 7 and 8. One of these is all empty: 0 0 0. One is all occupied: 1 1 1. And 
there are six more for a total of eight. If we turn this into a decimal number
it will have one of these values: 0, 1, 2, 3, 4, 5, 6, or 7. This number can 
be used as an *index* of the `rule` list. If our neighbrs are 1 1 0 (occupied / 
occupied / empty) in cells 6, 7 and 8 that gives us 4 + 2 + 0 = 6. `rule[6]` 
has a value of `True` so that will be `livingspace[7]` in the next time tick. 


To say this another way: When we convert three cells from binary to decimal it 
becomes our rule index. Let's work a couple more examples to see 
how this works. 


Suppose that cell 6 in `livingspace` is `True`. That is `livingspace[6] = True`. Suppose cell
7 is `False` and cell 8 is `True`. What should cell 7 be at the next time tick? These
cells 6, 7 and 8 are interpreted as binary digits in the 4s, 2s and 1s places. `True` is 1
and `False` is 0. So in this case `True False True` becomes
`1 0 1` in binary which is `4 + 1 = 5` in decimal. `rule[5]` is `False` so on the next time
tick cell 7 will be `False` or *empty*. 


Another example: Suppose cell 6 is `False`, cell 7 is `False` and cell 8 is `True`. Now
our binary digits are `0 0 1`. Cell 6 is the 4s digit, 
cell 7 is the 2s digit, cell 8 is the 1s digit. Our binary number 001 becomes `1` in decimal.
Looking it up we see that `rule[1] = True` so in this case cell 7 will be occupied (`True`) on 
the next time tick. 


We do not want to confuse the `livingspace` cells (which are `True` or `False`) 
with `rule` list values (which are *also* `True` or `False`). Both of them 
are lists but they play two different roles in our story here. Here is how they relate:

* At each time tick we loop over all the cells
* For each cell we look at its value and the value of its neighbors
* This gives us a number between 0 and 7 inclusive, like say '4'
* We use that '4' as an index to pick one element of the `rule` list
  * `rule[4]` which happens to be `True`
* This value `True` is copied from `rule` into `livingspace`


So the `rule` list is a *source* of `True` and `False` values that are copied into `livingspace`.


Hopefully it is clear now how all possible sequences of three cells connect to the `rule` list. 
No matter how they are arranged as a sequence of three `True/False` values: There will be a rule
entry for what we put in the middle cell of the three at the next time tick. 


So very good for cell 7; which refers also to cells 6 and 8. What about cell 8? Well for cell
8 we need to check cells 7, 8 and 9. For cell 9 we use cells 8, 9 and 10. So this is why we 
have a for-loop that goes across all the cells in `livingspace`. And notice that it does the 
calculation not using `livingspace` but rather it uses `oldlivingspace`. This is why we made
the copy of `livingspace`: If we calculated from `livingspace` and wrote the answer *back into* 
`livingspace` then we would mess up the calculation. It would be like adding two large numbers and
changing the digits of one of them before you were finished: You would get the wrong answer. 
To avoid that we work from the copy, called `oldlivingspace`. 


### Summary so far


So -- deep breath -- we have set up two for-loops, one inside the other. The first or outer
for-loop counts time, one time tick to the next. Within that for-loop is a second or inner
for-loop that scrolls across all the cells in the `livingspace` list of cells. For each of 
these cells it calculates the new value by using three adjacent cells to generate a key, 
called the `ruleIndex`. It then looks up the results and writes that into the `livingspace`
list before calling the `DrawDots()` function to show us the next time tick results. 


Now are we done? Not quite. There are a couple of things to tidy up.


### Indexing `livingspace`


For `i = 0` at the first cell (cell 0) of `livingspace` we have an index `i - 1` for
its neighbor to the left, which is `-1`. But allowed indices (we thought) run from
0, 1, 2, ..., nSpaces - 1. Notice `-1` is not an option as far as we know. Furthermore
that neighbor to the left is actually the one at the very far right end with index
`nSpaces - 1` (because `livingspace` wraps around like a bracelet or a ring). 


Ok so what do we do about this? The good news is: We don't need to do anything special
because Python already takes care of this.


In Python you can use an index of -1 to mean *the very last element of the list*. 
In other words Python has a built-in wrap-around for lists. That is why it is ok to use 
`livingspace[-1]` or `oldlivingspace[-1]`. This
is interpreted as `livingspace[nSpaces - 1]` which is just the last element of the list.
It is just what we want. This leaves us just one more problem which is what happens 
with the neighbor to the *right* at the very far right side of the `livingspace` list.


For the cell to the *right* of cell `i` we have the index `i + 1` we can run into trouble 
at the very end of the loop. If the biggest value of `i` is `nSpaces - 1` then we would
have index `nSpaces` which does not exist. There is not a wrap-around trick in Python like 
there was above. Instead we fix the index by using `(i + 1) % nSpaces`. This uses the 
**remainder** or **modulo** function to change that index to `0` which is what we want. 
You can look this up in your *Python for Kids* book if you like: The modulo operator `%`. 
It keeps us out of trouble at the far right edge of 'livingspace'. 


That's it as far as understanding the code. Let me know if you have questions. 


### Next-to-last item


Notice that the `rule` list has eight elements, each one either `True` or `False`. The rule
that I chose is called Rule 90. (See if you can figure out why.) You can change this rule
to be any sequence of eight `True` or `False` values that you like. 


Here is a first challenge for you: Try a few alternative rules to see if you can produce 
some other interesting patterns. 


Here is a second challenge for you: Come up with an idea for a rule and see if you can 
convert that into a `rule` list that does precisely what you expect. 


### Last item


You may recall that we started off this year with a project that filled in the Pascal triangle. 
There is a simpler version of the Pascal triangle where you only worry about even/odd. The `1` at the 
very top is odd so you draw that as a dot. Maybe an even number is just a blank space. So...
you can imagine everywhere else in the top row is zeros 
which are even. You know that odd + even = odd, even + odd = odd, odd + odd = even, and even + even = even. 
This is a rule; just like in our program; so now you can write out this new version of the triangle 
using only dots and blanks.  
