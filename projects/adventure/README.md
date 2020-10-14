# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/adventure)


### Overview

Here is a text adventure game:


```
print('You are outside a castle full of monsters. The entrance is just wide enough for you to squeeze in.')
print('The wind whistles and cold rain is soaking you. Inside you see a fire... but you hear scary sounds.')

action = input('What do you do? ')
if action == 'run away':
    print ('You win! Congratulations on your great fountain of wisdom!')
else:
    print ('The monsters get you... sorry but you lose.')
````

Now the trick is to come up with a more interesting version of this game...


### Details

One way to approach these games is to turn the players' action phrase (the response to 'What do you do?') into
a list of words. Then you can search for certain key words in that list to decide that the player probably had
the right idea. 

This makes use of two useful things in Python: The **split** method for strings and the **in** 
function for lists. In this example the player should light a fire in the fireplace because this will scare a 
cat who is sleeping in there; and the cat has a clue on her collar. 

```
while True: 
    print('you are in the library. There is a dark fireplace here and a desk with locked drawers.')
    action = input('What do you do?')
    action_list = action.split()
    if 'light' in action_list and 'fire' in action_list: 
        print('Finding matches and wood nearby you light a fire in the fireplace.')
        print('As you do so a terrified cat leaps out of the fireplace and runs across the room.')
    else: 
        print('That doesn't seem to help much.')
```

Often these text adventures require you to pick up useful items. You can keep these in a separate list called
**inventory**.
