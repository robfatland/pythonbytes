## 1dca lesson Part 5

### Before we get started

The code for this program may seem mysterious or a bit complicated. This is why I broke it down into five 
parts, to try and make it a more gradual hill to climb. My goal is to show you what is possible with just
a few lines of code without staying in the area of super-basic. There are two good results of this approach; 
at least I hope. First this code is from real computer science. It is an open door into a world of ideas 
that stretch our imagination and make new discoveries possible; which is fun. 


Second: My hope is that by seeing certain patterns in the Python code -- the way it is written -- you will
begin to see the elegance of computer programming. If you listen to an unfamiliar language being spoken 
it might not make sense at first but it certainly can sound very beautiful; so then there is the opportunity
to learn that language and make those wonderful sounds as well. 


So before going any further: Thank you for giving this a try! I appreciate your adventurous spirit. 


### What did that rule do? 


Remember that our rule was written as a list of boolean values `True` and `False`: 

```
    rule = [False, Tre, False, True, True, False, True, False]
````

This means that if we say `print(rule[3]))` we should see **True**. So here is the key idea: 

***Each of the eight values of the `rule` list is a possible new value for a cell in `livingspace`.***
