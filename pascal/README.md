# Python Pascal Triangle

## Overview

To remind you we want our program to print the Pascal triangle like this:

```
                 1
             1       1
         1       2       1
     1      3        3       1
 1       4       6       4       1
```

and so on. We have a start! See the bottom of this page for a reminder on what we did at our first meeting.
Now to finish our project we need four things:

- First we need a way to `print()` lines that do not have a linefeed built in (that skips to the next line)
  - This is so we can glue together each row of the triangle from its pieces so it looks like this:

```
 1       4       6       4       1
```

instead of like this

```
 1
         4
                 6  
                         4
                                 1
```

- Second we need a way to `print()` bigger numbers the same size as small numbers...
  - `462` is three characters wide; and `5` is only one character wide
  - We want to add two spaces in front of the `5` so it lines up with `462` like so:

```  
     462
       5
```
  
- Thirdly we need a way to count automatically. For this we use a Python function called `range()`.

- Fourth and lastly: Suppose we have a row of the triangle as a Python list. We need a way of building the *next* row from that.

Remember to use IDLE!

## Part 1: Printing without a line feed

Try running this code:

```
print("fred")
print("flintstone")
print("was here")
```

That is what we probably expected. But we can change the print to not add the line feed at the end of 
`fred` so that `flintstone` prints directly after `fred`. Try this: 

```
print("fred", end="")
print("flintstone")
print("...was here")
```

This is almost perfect; there is still one small problem. See if you can fix it. 


## Part 2: Printing numbers the same width so they line up

Copy and run this code. It uses four variables. Bonus: What is their **type**?

```
a1 = 5385
a2 = 3
a3 = 12
a4 = 946728348

print('\nmessy version:\n')

print(a1, a1)
print(a2, a1)
print(a3, a1)
print(a4, a1)
```

Notice that the numbers are all jammed together and it is hard to read. What we need is a format
that lines everything up. Here is how to do this (add these lines below what you just did):

```
print('\npretty version:\n')

print('%9d' % a1, '%9d' % a1)
print('%9d' % a2, '%9d' % a1)
print('%9d' % a3, '%9d' % a1)
print('%9d' % a4, '%9d' % a1)

print('\n')
```

That is a little recipe that makes sure every number is 9 characters wide.


## Part 3: Counting using `range()`

The `range()` function counts for you. If you use `range(5)` in a Python program it will count
`0, 1, 2, 3, 4`. So it starts at zero and goes up to just below the number you give. In this case 
you gave it `5` so it stopped at `4`. Run this code:

```
my_counter = list(range(7))
print(my_counter)
```

You could also experiment with `range(2, 9)` and `range(4, 21, 3)` and even `range(19, -6, -2)`.
What do these do? 

As a final experiment what does this code do? 

```
q = 10
a = list(range(q))
for b in a:
    print(' ' * (30 - 2*b), 'cow')
```



## Part 4: Creating the next row from the current row


Suppose we have row 3 in a list called `row`. 

```
print(row)
[1, 2, 1]
```

This has three elements: 1, 2, and 1. The next row will have four elements. Let's create
a new row where all the elements are 1. Check and see if this works: 

```
new_length = 4
new_row = [1]*new_length
print(new_row)
```

Now print out each element of the `new_row` list:

```
print(new_row[0])
print(new_row[1])
print(new_row[2])
print(new_row[3])
print(new_row[4])
```

This code will give you an error. It has a bug that you will need to fix. 

Finally notice that you could write:

```
new_row[1] = row[0] + row[1]
print(new_row[1])
```

Now you have all the pieces you need to finish this project; but there is still some careful thinking and
programming to do. We will meet online (I hope) on Monday at 6 pm to put everything together. If that does not
work out then we will meet Wednesday at 7 and continue then.



## Solution


Here is a solution... but it is hidden for now! We will put our final solution here once we have it!


## Bonus challenge


If you finish this Pascal project and are interested in a similar challenge: Try building a counting spiral. It simply counts from
1 to 36 placing the numbers in a square spiral, for example like this: 

```
  21   22    23    24    25    26
  20    7     8     9    10    27
  19    6     1     2    11    28
  18    5     4     3    12    29
  17   16    15    14    13    30
  36   35    34    33    32    31
```

Of course you want to do this as a code that figures everything out; not as six print statements! 

## What we began with

* Rob's first rule of computer programming: Put your computer away (get out a piece of paper)
* Rob's second rule of computer programming: Don't do what you are trying to do; instead do something easier.


Our project is to print out a Pascal triangle, like ten rows of it. To make progress we reminded ourselves
of two programming ideas. First that variables are like little buckets with a label and some contents and 
a `type` such as *integer* or *string*. The second programming idea is that Python programs break down into
statements which run in order from the top down. When we include loops this sometimes jumps around.


The Pascal triangle starts with a `1` in the middle of the page, at the top. There are invisible zeros on either
side so that when we add two things together we get all zeros except for `0 + 1 = 1` and `1 + 0 = 1` so that the
second row has two `1`s in it: `1      1`. From here we find the next row is `1      2      1` and so on; so we
practiced building a few rows of the triangle. 


Then we asked the question "How would you write a computer program to print this triangle?" We were very puzzled 
as it seemed like a complicated task; so this is when we opened up our computers and began doing simpler things
to build up pieces needed for the project. 


We proceeded to remember our Python syntax starting with this program: 


```
for i in ['pig', 'dog']:
    print(i)
```

Before running each bit of code we first predict what it will do. Here we have a list of two strings so we 
become familiar with how the variable `i` takes on each value in the `list` in turn. 


Next we ran variations of this where instead of strings we put numbers (integers) in the list: 


```
for i in [0, 5, 10, 15, 20, 25]:
    print('m'*i, 'horse')
```

Finally we reversed the order of the numbers in the list:


```
for i in [25, 20, 15, 10, 5, 0]:
    print('m'*i, 'horse')
```

From here we had a little bit of an ***Aha!!*** because we can see the indent getting less and less; just like we 
would need for the Pascal triangle. That is pretty much all we got going on the first session.




