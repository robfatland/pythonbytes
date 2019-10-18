To remind you we want our program to print the Pascal triangle like this:

```
                 1
             1       1
         1       2       1
     1      3        3       1
 1       4       6       4       1
```

and so on. We have a start! And now to finish our Pascal Triangle project we need three things:

- A way to `print()` lines that do not have a <linefeed> built in
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

- A way to print() bigger numbers the same size as small numbers...
  - `462` is three characters wide; and `5` is only one character wide
  - We want to add two spaces in front of the `5` so it lines up with `462` like so:

```  
     462
       5
```
  
- Lastly suppose we have a row of the triangle as a list. We need a way of building the *next* row.

Use IDLE...

```
row = [1]

for q in range(1, 11, 1):
    q_indent = q*(-3) + 30
    print(q_indent*' ', end = '')
    for i in range(q): print('%3d' % row[i] + '   ', end = '')
    print('\n')
    
    newrow = [1] * (q + 1)
    for i in range(1, q, 1):
        newrow[i] = row[i-1] + row[i]
    row = newrow[:]
```
