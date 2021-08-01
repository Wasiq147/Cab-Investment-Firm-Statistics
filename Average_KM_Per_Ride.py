import numpy as np
import matplotlib.pyplot as plt
from Cab_Data_Statistics import *
cab_yellow = [yellow_avgKM]
cab_pink = [pink_avgKM]

fig = plt.figure()
ax1 = fig.add_subplot(111)

plt.ylabel('City')
plt.xlabel('Average Rides Travelled')
plt.title('Average Rides Traveled in Each City')
ax1.scatter(cab_yellow, city, s=10, c='yellow', marker="s", label='Yellow Cab')
ax1.scatter(cab_pink, city, s=10, c='pink', marker="s", label='Pink Cab')
plt.legend(loc='upper left');
plt.grid()
plt.show()