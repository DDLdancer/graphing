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
min=100000000 # TODO: how to display large number in python3
while data != '':
    data, xi, yi = map(float, data.split())
    speed = data / yi
    if (speed < min):
        min = speed
    nodes.append(xi)
    x.append(log(xi, 2)) # use log on number of nodes
    y.append(log(speed / min, 2))
    data = f.readline()

# disable x axis number
plt.xticks([])

plt.plot(x, y)

for i in range(len(nodes)):
    plt.annotate(f"{nodes[i]:.0f}", (x[i], y[i]))

plt.ylim(bottom = 0)
plt.savefig(sys.argv[1].split(".")[0])
