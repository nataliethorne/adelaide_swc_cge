#all:


# Default values for n
n=100

#clean:
#	rm files*  



output.txt: source.fas mutant.fas 
	python generate_substring.py $^ $n $@


# $^ means insert all dependencies


