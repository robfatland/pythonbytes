# PythonBytes Project In-Depth


## Project Euler


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/euler#pythonbytes-project-in-depth)



[Here is a link to the Project Euler website](https://projecteuler.net)


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/euler/euler.png" alt="drawing" width="280"/>


### Overview


If I ask you to solve an arithmetic problem like 'What is 7 + 3?' you will say '10' since you have a very fine
calculator in your head. But if I ask you to sum the squares of all the numbers from 1 to 93,000 you will probably
ask for a calculator... or reach for a computer with Python. If you asked *me* to solve that problem I would
say 'That is a very *boring* problem; can you give me something more interesting to do?' and **that** is precisely
the idea of **Project Euler**: To pose interesting problems that can be solved with the help of a computer. 


Below we list out a number of such projects that we have tried out. The cool thing about doing these problems
is that you get an answer that you can check by entering it into the answer space at Project Euler.



### Projects and Problems We Recommend

**Problem 1: Sum of Multiples of 3 and 5**

*If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.*

### Spoiler Alert!

If you want to continue under your own power: Don't read any further; the next section has spoilers.
Make sure to give the problem a try before looking at spoilers.

```
#Problem 1: Sum of Multiples of 3 and 5

def euler(x):
    total = 0
    for i in range(0,x):
        if i % 5 == 0:
            total = total + i
        elif i% 3 == 0:
            total = total + i
    print (total)
euler(10) # you will get 23
euler(1000) # you will get 233168
```

