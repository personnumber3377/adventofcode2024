

'''

def check_conditions(l1):
	if len(l1) < 2:  # A single-element list is trivially valid
		return True

	increasing = decreasing = True

	for i in range(1, len(l1)):
		diff = l1[i] - l1[i - 1]

		# Check differences
		if not (1 <= abs(diff) <= 3):
			return False  # Invalid difference, exit early

		# Check monotonicity
		if diff < 0:
			increasing = False
		if diff > 0:
			decreasing = False

		# If neither increasing nor decreasing, exit early
		if not (increasing or decreasing):
			return False

	return True  # Both conditions hold

'''


def check_conditions(l1):
	if len(l1) < 2:  # A single-element list is trivially valid
		return True

	increasing = decreasing = True

	for i in range(1, len(l1)):
		diff = l1[i] - l1[i - 1]

		# Check differences
		if not (1 <= abs(diff) <= 3):
			return False  # Invalid difference, exit early

		# Check monotonicity
		if diff < 0:
			increasing = False
		elif diff > 0:
			decreasing = False
		else:
			return False # The list has two consecutive elements of the same value. This is invalid.
		# If neither increasing nor decreasing, exit early
		if not (increasing or decreasing):
			return False

	return True  # Both conditions hold


def solve(lines: list[str]) -> int: # Solve function.
	
	return sum([1 if check_conditions(list(map(lambda x: int(x), line.split(" ")))) else 0 for line in lines])



if __name__=="__main__":

	fh = open("input.txt", "r")
	lines = fh.readlines()
	fh.close()

	res = solve(lines)

	print("Result: "+str(res))

		
	exit(0)
