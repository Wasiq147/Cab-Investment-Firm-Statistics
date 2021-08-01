import matplotlib.pyplot as plt
from Dataset_Complete import *

labels = 'Card', 'Cash'
sizes = [Payment.count('Card'), Payment.count('Cash')]
colors = ['blue', 'green']
explode = (0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=100)

plt.title('Transaction Payment Type')
plt.axis('equal')
plt.show()