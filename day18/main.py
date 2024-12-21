#!/bin/python3

# This is my solution to https://adventofcode.com/2024/day/18



WIDTH = 70
HEIGHT = 70

def solve(lines: list[str]) -> int: # Solve function.

	maze_matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] # Maybe this should suffice????

	# Populate the matrix ("corrupt" spaces)
	for line in lines:
	x,y = [int(x) for x in]

	return 0

if __name__=="__main__":

	fh = open("input.txt", "r")
	lines = fh.readlines()
	fh.close()

	res = solve(lines)

	print("Result: "+str(res))

		
	exit(0)
