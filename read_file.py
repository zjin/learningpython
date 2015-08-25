import fileinput

filePath = "input.txt"

lines = 0

for line in fileinput.input(filePath):
	lines += 1

print lines
