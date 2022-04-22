import matplotlib.pyplot as plt
import sys

f = open(sys.argv[1], 'r')
xs = []
ys = []

data = f.readline()
while data != '':
    x, y = map(float, data.split())
    xs.append(x)
    ys.append(y)
    data = f.readline()

plt.xlabel("node number (2^x nodes)")
plt.ylabel("time")
plt.plot(xs, ys)
plt.ylim(bottom = 0)
plt.savefig(sys.argv[1].split(".")[0])
