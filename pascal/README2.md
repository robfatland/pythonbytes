# Final Notes for the Pascal triangle

Ok we are almost there with the Pascal triangle. This page has three parts: Finishing the program, adding the 
sum of each row, and describing a new problem. 

## Finishing the Program

### Review of `print()` for the triangle

Let's review what we need to finish the triangle. I will start with definite numbers for example and 
then I will change this gradually into variables in our code. 


Suppose you have printed rows 1 -- 4 like this: 


```
                     1
                 1       1
             1       2       1
         1       3       3       1 
```


Now you are printing row `5` of the triangle and so far you have printed the first three numbers:

`
```
  1     4     6
```

The next number you need to print is `4` because the entire row is `1  4  6  4  1`. Suppose you 
have the entire row calucalted in a list called `new_row`. (There is more on this below.)  
If everything is done correctly then `new_row` is the list `[1, 4, 6, 4, 1]` and the next number you want 
to print is `4` which is element 3 of `new_row`, or in other words `new_row[3]`. So far so good. 


The problem is that we don't get to write `new_row[3]` in our code. It is not flexible. Instead we have to
use a variable inside `[ ]`. This is just fine: We are inside a loop across the row so we have this variable
available to us. Let us suppose that there is an outer loop over 10 rows that uses the variable `i` like this: 


```
for i in range(1, 11):
```

This will make `i` be equal to `1`, then `2`, then `3`, ... all the way up to `11`. For the 5th line `i` is `5`.
Inside the `i` loop we use a second loop called the `j` loop, like this: 

```
    for j in range(i):
```

So when `i` is `5` the function `range(i)` will give us `0, 1, 2, 3, 4` for `j`. 


Ok so `i` is equal to `5` because this is row `5` and `j` has value `3` because the `j`-loop is running
across `0, 1, 2, 3, 4` and it has already done `0, 1, 2` and now it is `3`. We want to print `4` which is 
`new_row[3]` which is `new_row[j]`. So the print statement looks like this: 


```
        print("%3d" % new_row[j], "   ", end="")
```

Once we finish the entire row we need a line feed:

```
    print("")
```

### Making `row[]` and `new_row[]` lists 


The way I created the list `new_row` from the list `row` is described here. Also every time we finish printing
the new row (`new_row`) we want to copy it into `row`. Why? Because the next time we come around on the loop we
want to generate the ***next*** version of `new_row` from `row`. So we have to update `row` to be ready for that.
It is like building a volcano: The next layer of lava sits on top of all the previous layers of lava. 


We can begin outside of the loops by making `row` be an empty list:


```
row = []
```

Then we have a for-loop using `i` that goes from `1` to `10`. These are the rows of the triangle.


```
for i in range(1, 11):
```


Now let's create a new list that is all `1` values: 


```
    new_row = [1] * i
```

If we printed this after the first time it runs we would get `[1]` because `i` is `1 `. 
On the fifth time through the loop when `i` is `5` we would get `new_row` to be 
`[1, 1, 1, 1, 1]`. This is a good start on the Pascal triangle row. The first and last elements
are correct but the middle elements need to be fixed.  


How do we fix the middle three elements which are `new_row[1]`, `new_row[2]` and `new_row[3]`? 
One way to do it is to use a loop to make `new_row[]` correct. We do this before we do the 
`print()` stuff above. 


See if you can figure this out from here. If you get stuck you can keep reading.


#### Fixing the middle part of the list


Here is some useful code:


```
    for j in range(1, i - 1):
        new_row[j] = row[j - 1] + row[j]
```

When `i` is `5` we see that `j` will take on values `1, 2, 3`. That is good, just what we want. 
When `j` is `1` the `new_row` value `new_row[1]` will be calculated as `row[0] + row[1]`. 
Since `row` is `[1, 3, 3, 1]` this gives us `1 + 3` which is `4`. You can check that the other 
`new_row[j]` calculations in the `j` loop also work.  


#### Copying `new_row` into `row`


The simplest way to make `row` equal to `new_row` at the end of the loop is like this: 

```
    row = new_row[:]
```

The `:` inside the square bracket means `go through the entire list and make a copy of it`. 


## Extra challenge


At the start of each row, over on the very left-hand side: Print out the sum total of all the numbers
in that row. For the first row `[1]` this sum is `1`. For the second row `[1   1]` the sum is `2`. See 
if there is a pattern.

Here is some code that shows how you can use the `sum()` function to add up all the numbers in a list: 


```
a = [4, 5, 10]
my_sum = sum(a)
print(my_sum)
```

Would this code also work? 


```
a = [4, 5, 10]
print(sum(a))
```


What happens if you run this code: 


```
a = [4, 5, 'pig']
print(sum(a))
```


## Next problem

Our next problem to solve is... send me suggestions on slack!




