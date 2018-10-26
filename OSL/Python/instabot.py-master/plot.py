import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

x = []
y = []

with open("testfile.txt") as f:
    data = f.read()
data = data.split('\n')
names = [row.split(' ')[0] for row in data]
minutes = [int(row.split(' ')[1]) for row in data]
#print (names)
y_pos = np.arange(len(names))
plt.bar(y_pos, minutes, 1/4,color="blue")
plt.xticks(y_pos, names)
plt.xlabel('Date')
plt.ylabel('Minutes')
plt.title('Bot work time')
plt.show()    