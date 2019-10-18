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

and so on. We have a start! And now to finish our project we need three things:

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

- Second we need a way to print() bigger numbers the same size as small numbers...
  - `462` is three characters wide; and `5` is only one character wide
  - We want to add two spaces in front of the `5` so it lines up with `462` like so:

```  
     462
       5
```
  
- Thirdly and lastly: Suppose we have a row of the triangle as a Python list. We need a way of building the *next* row from that.

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

## Part 2: Printing numbers the same size

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


## Part 3: Creating the next row from the current row


## Solution

```
for q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    q_indent = q*(-3) + 30
    print(q_indent*' ', end = '')
    for i in range(q):
        print('%3d' % row[i], end = '')
        print('   ', end = '')
    print('\n')
    
    newrow = [1] * (q + 1)
    for i in range(1, q, 1):
        newrow[i] = row[i-1] + row[i]
    row = newrow[:]
```
