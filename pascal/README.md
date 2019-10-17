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
