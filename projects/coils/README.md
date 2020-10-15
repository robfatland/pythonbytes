# PythonBytes Project In-Depth


## Coils: Pythons makes them easily and they include loops


Looking for project work to reinforce your basics?  This is the place for you. 


### Starters: Write a program...

* ...that prints *`Lonna’s dog said “whuff!!”`*
* ...to print out the first 20 fibonacci numbers: `0, 1, 1, 2, 3, 5, 8, ...` and so on.
* ...to determine if a positive integer is a prime number
* ...that uses random numbers

```
from random import randint
print(randint(1,6)+randint(1,6))
```

### Next level up: Write a program with turtle graphics...

* ...that draws a simple optical illusion
* ...that watches some turtles wander around on the screen


### Trickier

* Input a number and then print that many fibonacci numbers
* Print ten rows of the Pascal triangle nicely
    * Also add up the numbers in each row to see if they form a pattern


### Definitely Tricky


* If you roll and add 3 dice the lowest possible is 3, highest is 18. Roll `n` dice the lowest is `n` and the highest is `6n`. 
    * Write a program to roll *n* dice 10,000 times in a row
        * Store the results in a list. 
        * Plot the results using a turtle. 
        * Compare what you see for `n = 1, 2, 3, 4, 5`.


* Subset counting in binary...
* Add up all the integers from 1 to 9,472
* What is the difference between `range(20)`, `range(4, 20)`, and `range(4, 20, 7)`? 


* Write program to play first one side; and the other side; of the number guessing game
    * **Chooser** picks a number from 1 to 100
    * **Guesser** tries to guess the number by saying a number 
        * **Chooser** reponds by saying 'Higher!' or 'Lower!' or 'Got it!' 
        * Track how many guesses were needed
        * The two players take turns being **Chooser** and **Guesser**
    * The program that plays as **Chooser** is probably easier to write first
    * The program that plays as **Guesser** is a little harder to write
    
    * You can combine both programs so that a human can first choose what they want to play as
    
* Write a computer program to play Nim.

* [Old Gold](https://nrich.maths.org/1209): Click on the link to learn how to play this game


### Graphics


Learn turtle graphics! Here are some challenges for you. 


* Write a program that draws your name
* Create two turtles that each follow their own path?
* Draw a boat on the ocean
* Look up some famous droodles; or invent your own; and draw them
    - I like "Ship arriving too late to save a drowning witch"
* Write a program showing a pencil drawing another pencil


* This one involves pursuit. 
    - Create two turtles named Alpha and Bravo. 
    - Place Alpha at (-150, -150)
    - Place Bravo at (150, -150)
    - Create a time for-loop that counts through 400 time ticks. 
    - Each tick: Alpha moves one pixel up and to the right. 
    - In the same tick: Bravo moves forward one pixel towards Alpha. 
    - Notice that as Alpha moves Bravo will have to keep adjusting the direction that she travels. 
        - The challenge is to make sure Bravo is pointed towards Alpha 

- Spacecraft trajectories
    - Choose two pairs of numbers as coordinates: `(x, y)` and `(u, v)`
    - Draw three arrows
        - An arrow from (0, 0) to (x, y)
        - An arrow from (0, 0) to (u, v)
        - An arrow from (0, 0) to (x + u, y + v)
    - This basic building block is a step towards spacecraft trajectories
    - Try introducing a clock where x, y, u, and v are changing: See coaches for more details


### Prime Race


These challenges have to do with prime numbers... so tread carefully.


Write a program that asks for an input number like 7 and then returns the 7th prime number (which is 17) as fast as it can. 


Look up the "Ulam spiral" and write a program to print it. Here is how it begins:


```
                        17          13
                            5     3   
                        19        2 11
                            7         
                              23       etcetera
```

### Probability

* What does this program do?

```
from random import choice
for i in range(10): print choice(['heads', 'tails'])
```

* Suppose you only have a fair coin that has a 0.5 probability of coming up heads and a 0.5 probability of coming up tails. That is: It comes up heads 50% of the time. How would you use this coin to accurately create an unfair coin that came up heads 37.2% of the time? Check your conclusion by writing and using a Python program.


### Games and diversions


* print out some **ascii art**
* Pig Latin translator
* Nim    
    * Nim uses a pile of stones, like 17
    * Players take turns removing one or two or three stones from any single pile
    * The player who takes the last stone (having no choice) loses that game
* Joke generator
* Magic 8 Ball
* Mastermind
* Hangman
* Yahtzee
