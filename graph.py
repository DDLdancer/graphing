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

# read data
data = f.readline()
min=sys.maxsize
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

# draw lines
ax.plot(x, y, label = "Actual")
ax.plot(x, y_ideal, label = "Ideal")
ax.set_xticks(x)

# set to log scaling
ax.set_xscale('log', base = 2)
ax.set_yscale('log', base = 2)

# make ticker none log based
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

# set limit for each axis
ax.set_ylim(bottom = 1, top = x[-1]/x[0])
ax.set_xlim(left = x[0])

# display line name
plt.legend()

# save the chart
plt.savefig(sys.argv[1].split(".")[0])