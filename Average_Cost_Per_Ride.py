import numpy as np
import matplotlib.pyplot as plt
from Cab_Data_Statistics import *
cab_yellow = [yellow_avgC]
cab_pink = [pink_avgC]

fig = plt.figure()
ax1 = fig.add_subplot(111)

plt.ylabel('City')
plt.xlabel('Average Cost per Ride')
plt.title('Average Cost per Ride in Each City')
ax1.scatter(cab_yellow, city, s=10, c='yellow', marker="s", label='Yellow Cab')
ax1.scatter(cab_pink, city, s=10, c='pink', marker="s", label='Pink Cab')
plt.legend(loc= 'center');
plt.grid()
plt.show()