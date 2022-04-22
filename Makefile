all: weak strong

weak strong:
	python3 graph.py $@.dat
	mv $@.png /mnt/d/graph/
