import matplotlib.pyplot as plt
import sys
from math import log

f = open(sys.argv[1], 'r')
x = []
y = []
nodes = []

# label axis
plt.title(f.readline())
plt.xlabel(f.readline())
plt.ylabel(f.readline())

data = f.readline()
while data != '':
    xi, yi = map(float, data.split())
    nodes.append(xi)
    x.append(log(xi, 2)) # use log on number of nodes
    y.append(yi)
    data = f.readline()

# disable x axis number
plt.xticks([])

plt.plot(x, y)

for i in range(len(nodes)):
    plt.annotate(f"{nodes[i]:.0f}", (x[i], y[i]))

plt.ylim(bottom = 0)
plt.savefig(sys.argv[1].split(".")[0])
