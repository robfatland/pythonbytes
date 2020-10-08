# PythonBytes Project In-Depth


## Coils


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/coils#pythonbytes-project-in-depth)


### What are Coils? Something Pythons make quite easily... that often include loops


Looking for project work to reinforce your basics?  This is the place for you. 

**Coil** challenges range from *pretty simple* to *a bit complicated*. 


### Starters

* Write a program that prints `*Lonna’s dog said “whuff!!”*`
* Write a program to print out the first 10 fibonacci numbers
* Determine what this program does by running it many times

```
from random import randint
print(randint(1,6)+randint(1,6))
```

* Write a program: Input a number n, then calculate and print n fibonacci numbers
* Write code to print ten rows of the Pascal triangle in a pretty and readable fashion
  * At the end of each row print a colon followed by the sum of all the numbers in that row
* If you roll 3 dice and add the results the lowest possible sum is 3 and the highest is 18. If you roll n dice the lowest is n and the highest is 6n. Write a program that rolls *n* dice 10,000 times and keeps track of the results in a list. Plot the results using a turtle. You can set the value of *n* at the top of the program or you can have this be an input. Compare your results for n = 1, 2, 3, 4, and 5. (Getting the turtle to draw your results is a very challenging and worthy project in itself!)
* You have a set of n objects, all different, placed in a row before you. You decide to count how many subsets of this set there are by placing either a black or a white pawn next to each object. A black pawn means the object is in the subset and a white pawn means that the object is not in the subset. Now two questions:
  * Does this suggest an easy way of calculating the total number of subsets?
  * What if anything does this have to do with previous challenges? 
* Add up all the integers from 1 to 9,472
* What is the difference between range(20), range(4,20), and range(4,20,7)? 
* Write program to play both sides of the number guessing game (this project is mentioend below in the cswonders section also)
  * **Chooser** picks a number from 1 to 100; and **Guesser** tries to guess it by saying a number. **Chooser** reponds by saying 'Higher!' or 'Lower!' or 'Got it!' and if you wish to keep score you count how many guesses were needed. The two players take turns being **Chooser** and **Guesser**. So the first challenge is to write a program that acts as **Chooser**.
  * You guessed it: Next write a program that plays the game as **Guesser**. Try and make it as skillful as you are. 
  * Now take both programs and combine them into a larger program. The human player first decides whether they want to be **Chooser** or **Guesser** and the program continues from there. 
* Write a computer program that plays Nim. This is described below in the cswonders section.
  * Here are five game challenges of increasing difficulty (no graphics necessary)
    * Guess a number from 1 to 100: Computer is the Chooser and responds **higher** / **lower** / **got it!**
    * Guess a number from 1 to 100: Computer is the Guesser and you (the player) are the Chooser
    * Nim: Set a pile of stones; the program and the human take turns removing 1 to 3 stones; the last one to remove a stone loses
    * Nim: Same as above but with three piles, for example with 9, 11, 13 stones
    * [Old Gold](https://nrich.maths.org/1209): Click on the link to learn how to play this game


### Turtle Graphics


Know turtle graphics? These are for you!


* Write a program that draws your name in some impressive way.
* Can you create two turtles that each follow their own path?
* Draw a boat on the ocean. Draw some famous droodles; or invent your own.
* What will the following program do? Check your answer by copying this into CodePad at cswonders.


```
import turtle
from random import randint
t0 = turtle.Turtle(); t0.color('blue'); t0.speed(0); 
t1 = turtle.Turtle(); t1.color('red'); t1.speed(0)
for i in range(100): 
    t0.forward(randint(20, 40)); t0.left(randint(0,359))
    t1.forward(randint(20, 40)); t1.left(randint(0,359))
```

* Create two turtles--one blue, one red--and have them start out facing one another, some distance apart. Make them walk towards one another. What happens?
* Write a program showing a pencil drawing another pencil. Look up Escher's *Drawing Hands*...
* This one involves pursuit. Create two turtles named Alpha and Bravo. Place Alpha at (-150, -150). Place Bravo at (150, -150). Create a time for-loop that counts through 400 time ticks. Each tick: Alpha moves one pixel up and to the right. In the same tick: Bravo moves forward one pixel towards Alpha. Notice that as Alpha moves Bravo will have to keep adjusting the direction that she travels. To get an idea of how to do this I will give you two options. Either explore this web page: https://docs.python.org/2/library/turtle.html or visit the [project ideas page for bugs](https://github.com/robfatland/pythonbytes/tree/master/projects/bugs#pythonbytes-project-in-depth). 
* Enter two pairs of numbers (x, y) and (u, v) and draw three arrows: An arrow from (0, 0) to (x, y), an arrow from (0, 0) to (u, v), and an arrow from (0, 0) to (x + u, y + v). This is a basic building block for creating a spacecraft trajectory planning program. Once you are good at this try changing those coordinates x, y, u, and v inside of for-loops in some interesting way.


### Prime Race


These challenges have to do with prime numbers... *the building blocks of reality!*... so tread carefully.


Write a program that asks for an input number like 7 and then returns the 7th prime number (which is 17) as fast as it can. 
The program should take an input as big as 78,498. We will time all contestant programs to determine which is the fastest. 


Now that you are good at prime numbers: Generate the Ulam spiral! This can be done with turtle graphics as you can print in color; or use regular print statements but only print the primes. The Ulam spiral begins at some (input!) number and counts upwards, printing the numbers so at to emphasize those that are primes.  It is common to begin at 41. Here is an example that goes from 1 to 25; the numbers follow a spiral path. It is not very interesting until you figure out how to emphasize the prime numbers.

```
                        17 16 15 14 13
                        18  5  4  3 12
                        19  6  1  2 11
                        20  7  8  9 10
                        21 22 23 24 25 etcetera
```

Here is the same thing but only printing prime numbers...

```
                        17          13
                            5     3   
                        19        2 11
                            7         
                              23       etcetera
```

Does a pattern emerge if you make the spiral much bigger? How about if you begin at 41 rather than 1?

### Probability

* What does this program do?

```
from random import choice
for i in range(10): print choice(['heads', 'tails'])
```

* Suppose you only have a fair coin that has a 0.5 probability of coming up heads and a 0.5 probability of coming up tails. That is: It comes up heads 50% of the time. How would you use this coin to accurately create an unfair coin that came up heads 37.2% of the time? Check your conclusion by writing and using a Python program.


### Data Science

These are more involved challenges that start to investigate the idea of data. For our purposes *data* means some form of 
information that we can look at using Python. If you want to explore any of these further: Maybe check in with the coaches.

* You are given a variable n that contains a very very long string of letters. Only four letters were used: A, C, G and T. They are in any order; for example the string begins n = ‘ACGGTATACCATGCT…’ and it continues for 10,000 letters. You also have a variable s = ‘ACAGTATAGTTT’, a shorter string of 12 letters. The question is “Where can this little string s be found in the big string n? 

### cswonders projects: Python I (see cswonders.com for complete instructions)

* print out some **ascii art**
* use turtle graphics and an input statement to create a birthday card for someone
* use turtle graphics to create colorful spirals
* use turtle graphics to create some snowflakes
* savings calculator: Watch your fortune grow
* MacArthur's math trick (this is a good basic project that everyone should do)
* Caesar Cipher (another good basic project that makes use of the modulus operator **%**)
* Pig Latin (manipulating strings with vowels and consonants)
* Guess the Number
  * First write the Chooser program that picks the number; and then responds 'Higher' or 'Lower' or 'Correct' to guesses 
  * Second then write the Guesser program where you are the Chooser and the program must zero in on your number with a guessing strategy
* Make a game. The game of Nim is a good one to begin with
  * Nim uses either one or two or three piles of stones
  * Players take turns removing one or two or three stones from any single pile
  * The player who takes the last stone (having no choice) loses that game
  * Here are five game challenges of increasing difficulty (no graphics necessary)
    * Guess a number from 1 to 100: Computer is the Chooser and responds **higher** / **lower** / **got it!**
    * Guess a number from 1 to 100: Computer is the Guesser and you (the player) are the Chooser
    * Nim: Set a pile of stones; the program and the human take turns removing 1 to 3 stones; the last one to remove a stone loses
    * Nim: Same as above but with three piles, for example with 9, 11, 13 stones
    * [Old Gold](https://nrich.maths.org/1209): Click on the link to learn how to play this game
    
### cswonders projects: Python II (see cswonders.com for complete instructions)

* Password generator
* Joke generator
* Magic 8 Ball
* Pico Fermi Bagels (a variant of the popular game Mastermind)
* Pictograph: This is a very challenging and interesting project where you could use turtle graphics combined with text
* Scrabble score
* Password protection
* Hangman
* Ninja Turtle
* Donut Clock
* Yahtzee: This is an excellent 'advanced' game project for three reasons
  * First you must accurately deal with the management of rolling the dice on each turn
  * Second you must accurately track all of the scoring details
  * Third if you are a crazy good programmer you could try to make the computer program one of the players
     * You would need to give it the ability to choose what to try for based on its initial roll of the dice
     * This is the sort of thing that is easy for humans to do but challenging to program
* Serpienski Triangles: This project is explored further in the **Fractals I** project here at pythonbytes
* Fractal Art: This project you may wish to speak with the coaches or with me to get going in a good productive direction
