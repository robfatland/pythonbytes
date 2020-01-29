## Part 4

### How to connect the `livingspace` list to a rule

For the next section of this project we will create a more interesting rule for what happens to `livingspace` from 
one moment in time to the next. Let's call these moments *time ticks*, like ticks on a clock, and imagine that we have a version
of the `livingspace` list at `time = 0` and we want to change this for one time tick later at `time = 1`. Then we will use
`livingspace` at `time = 1` to determine what it becomes at `time = 2` and so on.


You may recall that after we use `DrawDots()` to draw the current `livingspace` we copy this list into another
list called `oldlivingspace`. 

```
    oldlivingspace = livingspace[:]
```


We use `oldlivingspace` as a reference to determine the new `livingspace` at the
next time tick. 


Let's call each location in `livingspace` a *cell*. Each cell is either `True` or `False`. If it is `True` we imagine 
it is *occupied* and if it is `False` we imagine it is empty. Now for that more interesting rule for what happens to
each cell in `livingspace`. Here we go.

Our rule for cells:
The cell at the next time tick depends upon three cells at this time tick: The cell plus its two neighbor cells. 


Here are three cells in `livingspace` at list locations 6, 7 and 8:

```
       . . .    6      7      8    . . .
              False  True   False
```

The new value of cell 7 (at the next time tick) is going to depend on cell 7 at this time tick; and also on cell 6 
and also on cell 8 at this time tick. The new value of cell 8 will depend on cells 7, 8 and 9. The new value of 
cell 6 will depend on cells 5, 6, and 7. 


Here is a more extended picture. I use an `o` when a cell is `True` and a blank ` ` when it is `False`.
Again the top row shows the index values for the list.

```
  0    1    2    3    4    5    6    7    8    9    10
 [ ]  [ ]  [o]  [o]  [ ]  [ ]  [o]  [o]  [o]  [ ]  [o]   time = 0
 [o]  [o]  [o]  [o]  [o]  [o]  [o]  [ ]  [o]  [ ]  [ ]   time = 1
 ```

Here notice that `livingspace` contains 11 cells. We see this at two time ticks above. 
The `time = 1` version is calculated from the `time = 0` version. We use `oldlivingspace`
for this. The `time = 1` cell value at location 4 depends on the cell values at locations 
3, 4 and 5. 


Now let us notice a problem. The calculation works fine for cell locations 1, 2, 3, 4, 5, 6, 7, 8 and 9. 
Why? Because all of those cells have neighbor cells on both sides of them. However it does not work 
for cell locations 0 and 10. Think about this for a moment: How should we handle cell locations 0 and 10? 


One approach is to just ignore the missing locations. Since there is no cell location (-1) and no
cell location (11) we just ignore them when we calculate cell (0) and cell (10). 


We will take a different approach. We imagine that our living space wraps around like a bracelet so that cells
(0) and (10) are next to one another. Now the left-neighbor of cell (0) is cell (10) and the right neighbor
of cell (10) is cell (0). This is sometimes called wrap-around.


Now we can use our rule for every cell in `livingspace`. There is some tricky Python code to handle this.
As with the earlier parts of this project we will first see and then type in this tricky code; and then 
we will explain what it is doing. 


### Converting these ideas to code

We have three pieces of code to add to our program now. Since this is the new rule: First delete the 
old rule inside the time loop. The time loop should now look like this: 


```
for mytime in range(nTimeTicks):
    print('mytime is', mytime)
    DrawDots(livingspace, mytime)
    oldlivingspace = livingspace[:]
```

Notice I have made one change from before, in that first line. It now uses `nTimeTicks` in `range()`
rather than the number `6`. So make sure that change is in place. We set the value of `nTimeTicks`
up a little bit higher in the code. 


All three new pieces of code will live inside of this `mytime` loop so
again be sure to put them below all the code so far and be sure the code is
indented four spaces. Here is the first bit of code to add: 


```
    rule = [False, True, False, True, True, False, True, False]
```


Here is the code that goes below this. I am putting the second and third bits of code together:


```
    for i in range(nSpaces):
        i1 = i - 1
        i2 = i
        i3 = (i + 1) % nSpaces
        ruleIndex = 4*oldlivingspace[i1] + 2*oldlivingspace[i2] + 1*oldlivingspace[i3]
        livingspace[i] = rule[ruleIndex]
```

Now if everything is ok this should run (start drawing `livingspace` for several time ticks). 
This shows how our new rule works. 
If it is working you might wish to make `nSpaces` larger and make `nTimeTicks` larger. 
If it is not working remember you can look at the **console** tab on the right for error 
messages. 


Now the challenge -- for Part 5 -- is to understand what this code is doing. The check on 
understanding it is to change the rule and predict what the new rule will do. Notice that 
the rule is set up as a list with `rule = [False, True, False, True, True, False, True, False]`. 
At first look this might be rather mysterious. The other thing that is mysterious (at least
to me) is the `4` and the `2` and the `1` in the `ruleIndex = ` line. Why are those there? 


Tune in to **Part 5** to find out. Before you do you might take a moment to think about this, 
perhaps make a prediction. As a clue: See if you can figure out how to write the numbers from
zero to seven using base-2 notation. In base-10 these numbers are just 0, 1, 2, 3, 4, 5, 6, 7.
However in base-2 you only have two digits to use: 0 and 1. 
    

