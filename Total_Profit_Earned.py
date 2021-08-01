import numpy as np
import matplotlib.pyplot as plt
from Cab_Data_Statistics import *

cab_yellow = [yellow_sumP]
cab_pink = [pink_sumP]

fig, ax = plt.subplots()
bar_width = 0.35
X = np.arange(19)

p1 = plt.barh(X, cab_yellow, bar_width, color='yellow',
label='Yellow Cab')

p2 = plt.barh(X + bar_width, cab_pink, bar_width,
color='pink',
label='Pink Cab')

plt.ylabel('City')
plt.xlabel('Total Profit Earned')
plt.title('Total Profit Earned in Each City')
plt.yticks(X + (bar_width/2) , ("Atlanta", "Austin", 
"Boston", "Chicago", "Dallas", "Denver", "Los Angeles", "Miami", "Nashville", "New York", "Orange County", "Phoenix", "Pittsburgh", "Sacramento", "San Diego", "Seattle", "Silicon Valley", "Tucson", "Washington DC"))
plt.legend()

plt.tight_layout()
plt.autoscale(tight=True)
plt.show()