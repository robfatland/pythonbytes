<img src="https://github.com/robfatland/pythonbytes/blob/master/nim/nim_pile.png" alt="drawing" width="250"/>


# Nim Misere


Nim is a very simple game that will improve our Python programming skills in two stages. 
First we will write a program that plays the game legally; and then we will improve
that program so that it plays with skill.


## Rules of Nim


Two persons decide to play a game of Nim. Nim is a game of removing stones from a pile
in turns. Here is what happens.


* The players choose the number of stones in the pile 
  * From 8 to maybe 20 stones is a good range
* The players decide who is to go first (Player 1)
* Player 1 removes 1, 2 or 3 stones from the pile 
* Player 2 removes 1, 2 or 3 stones from the pile
* Players continue taking turns in this way until one player takes the last stone
  * That player who takes the last stone loses
  

## Rob's First Rule of Programming


Before trying to write some Python: Use a pencil and paper to play a few games of Nim. 
You can play just by yourself or you can play with a friend. After you play some games
of Nim what conclusions do you reach? 

> By the way: Losing by taking the last stone is called Nim Misere. You can also play
the game where the player who takes the last stone is the winner. No problems either
way but of course the strategy might change.


## Ingredients for this project


Our first goal is to write a computer program that plays Nim correctly. 
Here are some features of how this program should work. In this case 
we have Player 1 = the program and Player 2 = a human. 

* When the program begins: Ask the human for the number of stones
  * Make sure this is more than 4 and less than 30
* Make the human go first
  * You could also let the human decide if they want to go first or second
* Allow the human to take 1 or 2 or 3 stones
  * If they try to take a bad number of stones, like 5 or -3 stones: Don't allow this
* Once the player has chosen how many stones to remove: Print out the remaining pile 
  * For example: `13 stones remain     o o o o o o o o o o o o o`
* Now the program has to choose 1, 2, or 3 stones; so print this choice
  * `I choose to take 2 stones. 11 stones remain.`
  * Again print the pile of remaining stones `o o o o o o o o o o o`
* Keep repeating this until someone (the human or the program) takes the last stone
* Print out who won the game

### Input

stones_string = input("How many stones should we begin with?")

Now before we can begin we need to convert this *string* to a new variable of type *int*.


### Two useful ingredients


Here are two things that could be used in a Nim program: while and exit(). 


`while` is a Python key word that creates a simple loop. Suppose we have this code: 


```
a = 3
while a > 2:
    print ('a is still greater than 2')
```

This code will run forever! If you try it you might have to stop it using Ctrl-C. Let's do a nicer version: 


```
a = 3
while a < 10:
    print('a = ', a)
    a = a + 1

print('a is no longer less than 10. In fact a = ', a)
```

That takes care of `while` for a start. How about `exit(0)`? That stops the program
Suppose the player tries to remove a bad number of stones -- like 10 -- and you decide the program should
just stop in response. You can use `exit(0)` to do this: 

```
import os

os.exit(0)

print("never printed this bit i bet")
```


Now let's combine these two ingredients into one. Predict what this program will do before you run it. 


```
import os

a = 7
while a < 20: 
    print('a = ', a)
    a = a + 1
    if a > 15:
        print('time to quit!')
        exit(0)
        print('but this will not print because it comes after the exit()')

print('this will not print either')
```

### Choosing a random number from 1 to 3

`randint()` is a Python function that produces a random integer. 
Run this program to see how `randint()` works. The first lime `from random import randint` is a bit 
of magic that we will explain later. There was similar magic up above when we had `import os`. But
we won't worry about this at the moment. 

```
from random import randint

for i in range(20):
    my_random_number = randint(4, 8)
    print(my_random_number)
```

