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


Here is the Pascal triangle version.

```
# This uses a simple print() so the triangle is left-justified

for r in range(1,11):               # r will be 1, 2, 3, ..., 10
    row = []                        # row[] is an empty list
    for c in range(1, r + 1):       # c will be 1, 2, ..., r
        if c == 1:           
            row.append(1)           # left side of the triangle is 1
        elif c < r:
            row.append(row_above[c-2] + row_above[c-1])
                                    # middle of the triangle: add 2 numbers
        else:
            row.append(1)           # right side of the triangle is 1
        print("%4d" % row[-1], "  ", end = "")
    print("")

    # now the row[] list contains all the numbers in this row
    row_above = row[:]              # this makes row_above[] a copy of row[]
 ```
 
For this program to make sense it may help to know...
* Everything from the `#` onwards is a comment 
* `row[-1]` is a special Python of writing "the last element of the list `row[]`"
  * So if `row = [0, 3, 7, 12]` if we wrote `print(row[-1])` it would print `12`
* We can copy a list into a new variable using `new_list = old_list[:]`
  * This is another 'special' bit of Python 

Lists start indexing from `0`. This gets confusing when our rows start at row 1. The best
way I know to figure this out is to write everything out by hand. Here is an example of how
I write it out to myself.

* If `r = 7` and `c = 4` that means we are looking at the 4th number of row 7 of the triangle
* The value here will be the sum of the 3rd and 4th numbers of row 6 of the triangle
* In the program: row number 6 is held in a list called `row_above[]`
  * `row_above[]` is equal to `[1, 5, 10, 10, 5, 1]`. So `row_above[0] = 1` and `row_above[1] = 5` and so on. 
  * The third and fourth numbers in this list are `row_above[2]` and `row_above[3]`. These are both `10`.
  * This is why we have `row_above[c-2] + row_above[c-1]` in the code
    * When `c` is equal to 4 in row 7: Add `row_above[2]` to `row_above[3]`: `10 + 10 = 20`
    * So the fourth number in row 7 should be `20`
    * Row 7 is `1    6   15   20   15    6    1` so sure enough the 4th number is `20`. 
  

 
