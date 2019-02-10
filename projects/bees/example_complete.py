# This version runs on the repl.it website.
# Copy/paste this code into a new REPL (make sure in a Python 3 environment) and click the Run button

import requests                                 # this lets the program talk to the internet
import numpy as np                              # this gives you two-dimensional arrays: To represent your orchard
import matplotlib.pyplot as plt                 # this gives you the ability to make a plot of your results

# This function sends your drone to location (x, y, z) and returns the number of bees found there...
#   ...or if you drone got tangled up in the branches of a Baobab tree it returns 'drone lost'
def bees(x, y, z): 
  return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/' + \
        'default/dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text

# Un-comment this next line to check if 'the drones are working ok today'
# print(bees(2000., 2000., 50.))

nStops = 5                                   # This is the number of locations in each dimension (x and y) to visit by drone

dronecounts = np.zeros((nStops,nStops))      # This is the 2-dimensional array representing your orchard

z = 5.                 # The drones measure at z = 5 meters above the ground
lost = 0               # When we begin we have lost zero drones

# Now we simply use two (nested) loops to send out our drones
for i in range(nStops):
  for j in range(nStops):
    x = i*2000./(nStops - 1.)          # This is the x-coordinate for this drone to visit
    y = j*2000./(nStops - 1.)          #   ...and the y-coordinate
    
    while True:                        # This is a do-forever task but it will break once the drone reports back
      bcount = bees(x,y,z)
      if bcount == 'drone lost': lost += 1
      else: break
      
    dronecounts[i, j] = float(bcount)           # We notice that 'bcount' is a string so we must convert it to a float
    print(i, j, 'lost drones =', lost)          # This keeps track of how far along we are (and how many drones lost)


# This section of code creates a plot of the results and displays it as a little image at repl.it
fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
ax.set_title('My Baobab Orchard')
plt.imshow(dronecounts)
fig.savefig('graph.png')
