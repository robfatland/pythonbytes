The Pascal project is a little bit complicated. 
It combines Python `lists` with two `for`-loops. The outer `for`-loop has *another* `for`-loop inside, 
called the *inner* `for`-loop. The inner loop has to get bigger on each row. So a lot to figure out. 


Let's take a moment to write a simpler program. This one prints all of 
the locations on a chess board. The rows have numbers and the columns have
letters. First look at this code and figure out what it will do. Then 
run the program and see if it does what you thought. Does it make sense?


```
letters = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

print("\nchess board\n")

for i in range(1,9):
    print(' '*12, end = '')
    for j in range(8):
        square_label = letters[j] + str(i)
        print("%5s" % square_label, end = '')
    print("")
 ```   
 
 
 Next let's change one line of this program to make it resemble the Pascal program.
 Locate the change and predict what will happen. 
 
 
 ```
letters = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

print("\nchess board\n")

for i in range(1,9):
    print(' '*12, end = '')
    for j in range(i):
        square_label = letters[j] + str(i)
        print("%5s" % square_label, end = '')
    print("")
 ```   
 
 Notice that we used a list for the letters; but we used the counting variable `i` for the row numbers. 
 Before we could print the square labels like `f2` we had to build the `square_label` string. This 
 line of code changes the *type* of the integer `i` to a string using the `str()` function. 
 
 
 Finally let's take one more step towards the Pascal triangle program by re-writing our 
 chess board program one more time. Here is the new version; and it uses lists...
 
 
 (Rob left off here for the moment...)

 
