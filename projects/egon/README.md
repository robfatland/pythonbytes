# Friendly introduction

The town of Monte Carlo is located on the northwestern coast of the Mediterranean Sea. It is famous for casinos and opportunities to gamble. 
In short: It is full of probabilities and random chance! Here we present two coding challenges.

## Challenge One: Anchorhead

One fine day a pirate who has been attending a party feels tired and returns to the harbor to fall asleep in her hammock on board her boat. 
She heads towards the wharf. Her boat is tied up at the far end. (A wharf goes out from shore and boats tie up to it.) This wharf is 7 steps 
wide and 21 steps long. The pirate's ship is at the far end. Unfortunately it is dark and before she arrives at this wharf she bangs her head 
on an anchor secured to the bow of another boat. She will be ok but for the moment she is very dizzy.


If she can walk the 21 steps to reach her boat: All will be well. She will clamber aboard and fall asleep. The problem is that as she walks
the 21 steps to her boat: After each step forward she also stumbles one step sideways: Either to her left or her right at random. Too many 
stumbles to the left or to the right: You see the problem! She will tumble off the side of the wharf into the cold water. (There are no
other boats tied to this wharf at the moment you see.) What is the probability she makes it safely to her ship if she starts at the center 
of the wharf? Again the wharf is 7 steps wide... so she starts at step 4. If she takes four steps and each time stumbles one step to the 
right: She will only be 4/21 of the way to her boat and she will fall off the right side of the wharf into the cold water. 


Do her odds improve if she starts at the left side of the wharf? 


If you allow her to walk along the wharf once either she makes it to her boat or she falls off the side of the wharf. How can you turn this
single experiment into a *probability* that she makes it to her boat? 


If the wharf happens to be wider, like 9 steps instead of 7, how do her odds change?  What if the wharf is only 17 steps long? Is there a
simple formula for any wharf, say **A** steps wide and **B** steps long? 

The goal here (in addition to writing some tricky code) is to investigate how computer programs can help us investigate mathematical problems. 


## Challenge two: Egon


This story is a bit like our drunken pirate described above... except nobody is going to fall into the harbor. It concerns an artist named Egon.


Egon is a painter and a poet. He lives in the beautiful town of Monte Carlo by the sea. In the center of this town is the town square, a large flat brick plaza. 
Egon wishes to paint something on the town square but he does not know what... until one day he finds a discarded dice. He discovers that when he rolls it
the top face comes up either 1, 2, 3, 4, 5 or 6. But he finds that he cannot reliably predict what that number will be. This gives him an idea for a painting. 


* Early one morning Egon sets three empty paint cans A, B and C on the ground to make a huge triangle in the town square
* He walks to some random location on the town square where he can see his three paint cans forming the corners of a large triangle, 137 feet to each side
    * The 137 feet is not important here; it is just for our amusement
* Egon rolls his dice.
    * On a 1 or a 2 he walks half way to paint can A
    * On a 3 or a 4 he walks half way to paint can B
    * On a 5 or a 6 he walks half way to paint can C
    * He then paints a dot on the ground at his feet
* From that new spot: Egon repeats the process: 
    * He rolls the dice
    * He uses the same method to select a destination paint can
    * He walks half way to that paint can 
    * He paints a dot

If Egon repeats the process 17 times he will have 17 dots. But he does not stop at 17. He keeps on going and going and going, rolling, walking half way, 
painting a dot, until the sun goes down. Here is the challenge in two parts:

***What do you suppose the resulting painting looks like?***

***Can you write a computer program to simulate Egon's painting?***
