import matplotlib.pyplot as plt
from Dataset_Complete import *

labels = 'Yellow Cab', 'Pink Cab'
sizes = [Com.count('Yellow Cab'), Com.count('Pink Cab')]
colors = ['yellow', 'pink']
explode = (0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=100)

plt.title('Total US Cab Market Share')
plt.axis('equal')
plt.show()