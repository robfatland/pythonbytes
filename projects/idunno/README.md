# PythonBytes Project In-Depth


[Here is a link to this page.](https://github.com/robfatland/pythonbytes/tree/master/projects/idunno#pythonbytes-project-in-depth)


### Overview


Here is a creature that lives in the ocean... and she has a problem... and she needs your help...


<img src="https://github.com/robfatland/pythonbytes/blob/master/projects/whales/humpback.png" alt="drawing" width="700"/>


### Details

A student -- when asked 'What can you do to help here?' -- replied 'ummmmm..... I dunno.......' This is exactly
right; and that's why we're here doing this project! As you develop tech skills you can help us change information
into a better world: For whales and humans as well. 


This project is a simple model of the ocean. First we want to create that watery world. Let's have it be small to
start with, 400 x 400 locations, in other words a grid of locations. One way to do this is with a list of rows. Each 
row is a list of 400 locations called columns. Let us call it ```ocean```. Run these two lines of code. You can
use any programming environment that supports turtle graphics; including [cswonders.com](http://cswonders.com). 


```
import numpy as np
np.random.seed(0)  # seed for reproducibility

ocean = np.zeros(shape=(400,400))
print("ocean ndim: ", ocean.ndim)
print("ocean shape:", ocean.shape)
print("ocean size: ", ocean.size)
print("ocean type: ", ocean.dtype)
```

Now we have an ocean, yay! 


Next let's print out a little patch of water, 5 x 5, and verify it is zeros: 


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


