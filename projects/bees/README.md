# PythonBytes Project In-Depth


### Please use Python 3 at http://repl.it for this project
#### Remember you have to create an account; and tell the website you are at Tyee Middle School


## Bees and Drones


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/bees#pythonbytes-project-in-depth)


### Overview

Farmers like to see bees (particularly honey bees) in their fields and orchards because the bees help pollinate the plants.
This results in a bigger harvest. 


In this project we imagine that you are a farmer and you happen to own an unlimited supply of drones. These
you can send to various locations in your orchard where they can count how many bees are nearby. (They listen 
to the buzzing.)


You goal is to find places where there are lots of bees clustered together. This is called a hive. Once you know
where the hive is you can visit it and cultivate the bees. To learn more about this
you can read [this article](https://en.wikipedia.org/wiki/Swarming_(honey_bee)).


The challenge of this project is to use Python to send your drones out into your orchard to count bees.
Try to find all of the hives but also keep track of how many drones you lose. The best program will win a
special Bee Prize at the end of the year. 


### Details


Somewhere on the internet I have installed a little program that acts like a Python function. You
send it a drone location and it tells you how many bees the drone counted... or it returns 'drone lost'
meaning your drone got stuck in a Baobab tree. We will use coordinates `(x, y, z)` where `x` and `y`
are locations in the orchard between 0 and 2000 meters. `z` will be height above the ground in meters. 
Baobabs can grow as high as 30 meters. 


Now let's ask "how many bees are at (x, y, z)" and see what comes back. Paste this into a
browser window: 


```
https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/dronebees?x=12&y=16&z=4
```

Notice that at the very far right it gives what x, y and z are.


I just did this and what I got back looked like a blank web page... until I noticed the number **8** in the upper left corner. 
So apparently there are 8 bees at the coordinates ```(x, y, z) = (12, 16, 4)```. What happens if I hit refresh?
This time I got 5 bees. So the response changes, presumably because the bees are flying around looking for flowers. 
Try changing the values for x, y and z to see what comes up. 


```
# Here is a simple program to test the drones ability to count bees in your orchard
import requests
def bees(x, y, z): 
    return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/default/' + \
        'dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# The function bees() returns a string, not an integer, not a float 
myResult = bees(10, 17, 4)
print(myResult)
```


When this runs properly it will either return a number of bees or it will return 'drone lost'. 


The challenge of this project is to think about the logic for locating the bee hives. Since the lost drones
cost some money you would like to be efficient in your search. 


Notice that you can augment your Python program with an incredibly powerful computer: You can use your own brain
to make suggestions. Good luck!


To see a solution to this Project look at the file (in this folder) called `example.py`.


