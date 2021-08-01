import matplotlib.pyplot as plt
from Dataset_Complete import *

labels = 'Male', 'Female'
sizes = [Gender.count('Male'), Gender.count('Female')]
colors = ['red', 'blue']
explode = (0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=100)

plt.title('Gender Diversity in Service Usage')
plt.axis('equal')
plt.show()