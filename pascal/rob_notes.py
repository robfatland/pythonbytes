import sys

print('range(7) gives:', range(7))

my_counter = list(range(7))
print('list(range(7)) gives:', my_counter)

for i in my_counter:
    print(100 - i*i)

sys.exit(0)

print("I am going to break", end="")
print("this print statement into two parts.")
print("   (that was ", end = "")
print("easy)\n\n\n")

first_row = [1]
second_row = [1]*2
third_row = [1]*3
fourth_row = [1]*4
print('the first row is', first_row)
print('the second row is', second_row)
print('the third row is', third_row)
print('the fourth row is', fourth_row)

row = first_row[:]
print('\na new copy of the first row:', row, '\n')

row = [1]

for q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    q_indent = q*(-3) + 30
    print(q_indent*' ', end = '')
    for i in range(q):
        print('%3d' % row[i], end = '')
        print('   ', end = '')
    print('\n')
    
    newrow = [1] * (q + 1)
    for i in list(range(1, q, 1)):
        newrow[i] = row[i-1] + row[i]
    row = newrow[:]

a1 = 5385
a2 = 3
a3 = 12
a4 = 946728348

print('\nmessy version:\n')

print(a1, a1)
print(a2, a1)
print(a3, a1)
print(a4, a1)

print('\npretty version:\n')

print('%9d' % a1, '%9d' % a1)
print('%9d' % a2, '%9d' % a1)
print('%9d' % a3, '%9d' % a1)
print('%9d' % a4, '%9d' % a1)

print('\n')

print("fred", end=" ")
print("flintstone")
print("...was here")

row = [1]
for q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    q_indent = q*(-3) + 30
    print(q_indent*' ', end = '')
    for i in list(range(q)):
        print('%3d' % row[i], end = '')
        print('   ', end = '')
    print('\n')
    
    newrow = [1] * (q + 1)
    for i in range(1, q, 1):
        newrow[i] = row[i-1] + row[i]
    row = newrow[:]

q = 10
a = list(range(q))
for b in a:
    print(' ' * (30 - 2*b), 'cow')

new_length = 4
new_row = [1]*new_length
print(new_row)
