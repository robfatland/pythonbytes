# This section of code: Keep as-is
import requests, numpy as np, matplotlib.pyplot as plt
def bees(x, y, z): return requests.get('https://52t7suregg.execute-api.us-east-1.amazonaws.com/' + \
        'default/dronebees?' + 'x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)).text


# Test code. Note: This will occasionally give you 'drone lost' as the result
# print(bees(2000., 2000., 50.))



# This is where you modify the code; check with a coach for more details
nStops = 5
dronecounts = np.zeros((nStops,nStops)) 
# result = bees(x, y, z)
# dronecounts[i, j] = float(result)



# This section of code: Keep as-is
fig = plt.figure(figsize=(6, 3.2)); ax = fig.add_subplot(111)
ax.set_title('My Baobab Orchard'); plt.imshow(dronecounts)
fig.savefig('graph.png')


