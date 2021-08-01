import numpy as np
import matplotlib.pyplot as plt
from Dataset_Complete import *
from Indexing_Code import *
cab_yellow = [Y_Atlanta, Y_Austin, Y_Boston, Y_Chicago, Y_Dallas, Y_Denver, Y_Los_Angeles, Y_Miami, Y_Nashville, Y_New_York, Y_Orange_County, Y_Phoenix, Y_Pittsburgh, Y_Sacramento, Y_San_Diego, Y_Seattle, Y_Silicon_Valley, Y_Tucson, Y_Washington]
cab_pink = [P_Atlanta, P_Austin, P_Boston, P_Chicago, P_Dallas, P_Denver, P_Los_Angeles, P_Miami, P_Nashville, P_New_York, P_Orange_County, P_Phoenix, P_Pittsburgh, P_Sacramento, P_San_Diego, P_Seattle, P_Silicon_Valley, P_Tucson, P_Washington]

fig, ax = plt.subplots()
bar_width = 0.35
X = np.arange(19)

p1 = plt.barh(X, cab_yellow, bar_width, color='yellow',
label='Yellow Cab')

p2 = plt.barh(X + bar_width, cab_pink, bar_width,
color='pink',
label='Pink Cab')

plt.ylabel('City')
plt.xlabel('Completed Rides')
plt.title('Completed Rides in Each City')
plt.yticks(X + (bar_width/2) , ("Atlanta", "Austin", 
"Boston", "Chicago", "Dallas", "Denver", "Los Angeles", "Miami", "Nashville", "New York", "Orange County", "Phoenix", "Pittsburgh", "Sacramento", "San Diego", "Seattle", "Silicon Valley", "Tucson", "Washington DC"))
plt.legend()

plt.tight_layout()
plt.autoscale(tight=True)
plt.show()