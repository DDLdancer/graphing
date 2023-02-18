import matplotlib
import matplotlib.pyplot as plt
import sys
from math import log

f = open(sys.argv[1], 'r')
x = []
y = []
y_ideal = []
nodes = []

fig, ax = plt.subplots()

# label axis
ax.set_title(f.readline())
ax.set_xlabel(f.readline())
ax.set_ylabel(f.readline())

data = f.readline()
min=100000000 # TODO: how to display large number in python3
while data != '':
    data, xi, time = map(float, data.split())
    speed = data / time
    if (speed < min):
        min = speed
    nodes.append(xi)
    x.append(xi) # use log on number of nodes
    y_ideal.append(xi/x[0])
    y.append(speed / min)
    data = f.readline()

ax.plot(x, y, label = "Actual")
ax.plot(x, y_ideal, label = "Ideal")
ax.set_xticks(x)

ax.set_xscale('log', base = 2)
ax.set_yscale('log', base = 2)

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

# label on the chart
# for i in range(len(nodes)):
    # plt.annotate(f"{nodes[i]:.0f}", (x[i], y[i]))

ax.set_ylim(bottom = 1, top = x[-1]/x[0])
ax.set_xlim(left = x[0])

plt.savefig(sys.argv[1].split(".")[0])
