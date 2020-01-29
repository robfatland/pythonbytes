## 1dca lesson Part 5

### Before we get started

The code for this program may seem mysterious or a bit complicated. This is why I broke it down into five 
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

This means that if we say `print(rule[3]))` we should see **True**. So here is the key idea: 

***Each of the eight values of the `rule` list is a possible new value for a cell in `livingspace`.***

Ok what does this mean? Why *eight* values and not nine? Let's think about cell number 7 like we
did before. Cell number 7 is going to have a new value at the next time tick: Based on what is found
in cell 6, cell 7 and cell 8. That is: In cell 7 and in its two neighbors. Let's describe every 
possibility for these cells. I will use `o` for a cell that is occupied and `-` for a cell that is 
empty. 

```
location  6   7   8
          -   -   -        all three cells are empty
          o   -   -        cell 6 is occupied, 7 and 8 are empty
          -   o   -        only cell 7 is occupied
          o   o   -        ...and...
          -   -   o        ...so...
          o   -   o        ...on...
          -   o   o        ...until we reach...
          o   o   o        all three cells are occupied
```

Now let us examine the numbers 0, 1, 2, 3, 4, 5, 6 and 7 written in base-2 or binary notation.

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

If we compare these two listings we notice that the possibilities for cells 6, 7 and 8 match up
perfectly with the base-2 numbers for 0 through 7. This means that we can use cells 6, 7 and 8
as a three-digit binary number; and when we convert it to decimal it becomes the rule index. That 
is, we use it to look up the results in our `rule` list. Let's work a couple of examples to see 
how this works. 


Suppose that cell 6 in `livingspace` is `True`. That is `livingspace[6] = True`. Suppose cell
7 is `False` and cell 8 is `True`. What should cell 7 be at the next time tick? We will make
cells 6, 7 and 8 be binary digits in the 1s, 2s and 4s places. So `True False True` becomes
`1 0 1` in binary which is `4 + 1 = 5` in decimal. `rule[5]` is `False` so on the next time
tick cell 7 will be `False` or *empty*. 


Another example: Suppose cell 6 is `True` as before, cell 7 is `True` and cell 8 is `False`. Now
our binary digits are `0 1 1`. Notice the order of the digits is reversed: cell 6 is the 1s digit, 
cell 7 is the 2s digit, cell 8 is the 4s digit. So now our binary number 011 becomes `3` in decimal.
Looking it up we see that `rule[3] = True` so in this case cell 7 will be occupied (`True`) on 
the next time tick. 


Hopefully it is clear now how all possible sequences of three cells connect to the `rule` list. 
No matter how they are arranged as a sequence of three `True/False` values: There will be a rule
for the middle cell at the next time tick. 


So very good for cell 7; which refers also to cells 6 and 8. What about cell 8? Well for cell
8 we need to check cells 7, 8 and 9. For cell 9 we use cells 8, 9 and 10. So this is why we 
have a for-loop that goes across all the cells in `livingspace`. And notice that it does the 
calculation not using `livingspace` but rather it uses `oldlivingspace`. This is the reason 
for the copy: If we were using `livingspace` and writing the answer in cell 7 that could change
the result for cell 8. We would be changing `livingspace` and breaking the algorithm in the 
process. So that is why we work from a copy to calculate `livingspace` at the next time tick. 


### Summary so far

So -- deep breath -- we have set up two for-loops, one inside the other. The first or outer
for-loop counts time, one time tick to the next. Within that for-loop is a second or inner
for-loop that scrolls across all the cells in the `livingspace` list of cells. For each of 
these cells it calculates the new value by using three adjacent cells to generate a key, 
called the `ruleIndex`. It then looks up the results and writes that into the `livingspace`
list before calling the `DrawDots()` function to show us the next time tick results. 


Now are we done? Not quite. There are a couple of things to tidy up.


### Indexing `livingspace`


For `i = 0` at the first cell (cell 0) of `livingspace` we have an index `i - 1`. In Python
you can use an index of -1 to mean *the very last element of the list*. In other words Python
has a built-in wrap-around for lists. That is why it is ok to use `livingspace[-1]`. 


For `i = nSpaces - 1` we use the index `(i + 1) % nSpaces`. This uses the **remainder** or 
**modulo** function. You can look this up in your *Python for Kids* book if you like. It 
has the effect of changing that index to zero (the index for the first list element) so again
we do not get into trouble. 


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
