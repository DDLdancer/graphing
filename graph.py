import matplotlib.pyplot as plt
import numpy as np
import sys

REPEAT=5

plt.rc('font', size=6)

# colors: https://matplotlib.org/stable/gallery/color/named_colors.html
nodes = ("1 nodes", "2 nodes", "4 nodes", "8 nodes")
data = {
    'Insert (64 tasks)': [[], "#003049"],
    'Assemble (64 tasks)': [[], "#D62828"],
    'Insert (60 tasks)': [[], "#F77F00"],
    'Assemble (60 tasks)': [[], "#EAE2B7"],
}

# Using readlines()
f = open(sys.argv[1], 'r')

title = f.readline()
ylim = float(f.readline())
 
count = 0

def read(node):
# Strips the newline character
    for i in range(4):
        f.readline()
        insert = []
        assemble = []
        for j in range(REPEAT):
            insert.append(float(f.readline()))
            assemble.append(float(f.readline()))
        data[f"Assemble ({node} tasks)"][0].append(sum(insert) / len(insert))
        data[f"Insert ({node} tasks)"][0].append(sum(assemble) / len(assemble))
    
read("64")
read("60")

x = np.arange(len(nodes))  # the label locations
width = 0.20  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in data.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement[0], width, label=attribute, color=measurement[1])
    ax.bar_label(rects, fmt='%.2f', padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (second)')
ax.set_title(f'{title} dataset assemble and insertion time by number of nodes')
ax.set_xticks(x + width, nodes)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, ylim)

# save the chart
plt.savefig(sys.argv[1].split(".")[0], dpi=300)