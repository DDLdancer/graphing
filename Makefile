DATA = $(wildcard *.dat)
OBJS = $(DATA:.dat=.png)

all: $(OBJS)

%.png: %.dat
	python3 graph.py $^
	mv $@ /mnt/d/graph/
