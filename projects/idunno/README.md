# PythonBytes Project In-Depth


## Suggest use **Python Turtle** environment at [repl.it](http://repl.it)

[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/idunno#pythonbytes-project-in-depth)


### Overview


Here is a creature that lives in the ocean... 


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/whales/humpback.png" alt="drawing" width="700"/>


### Details

This project is a simple model of the ocean. It creates this model ocean inside a Python program; and it has
both krill and whales swimming about. To learn more you can research the keyword `wator` or you can check
in with Rob. 


Here is some example code related to this project.

```
import numpy as np                  # this is a toolbox called num - py

ocean = np.zeros(shape=(400,400))
print("ocean ndim: ", ocean.ndim)
print("ocean shape:", ocean.shape)
print("ocean size: ", ocean.size)
print("ocean type: ", ocean.dtype)
```

To print out a little patch of water, 5 x 5, and verify it is zeros: 


```
print(ocean[51:56,287:292])
print('\nthat was the empty ocean...\n')
```

Now put the number 9 in the ocean: 

```
ocean[53,289] = 9
```

And print out the same ocean again: Check that the 9 is now there: 

```
print(ocean[51:56,287:292])
```

### Where next?

- Add a layer of plankton
- Add whales who swim about looking for plankton; which they eat.
- Give the plankton sunlight so they can grow


