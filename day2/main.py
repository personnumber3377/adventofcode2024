

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


PART = 2

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


def check_conditions_fault_index(l1):
	if len(l1) < 2:  # A single-element list is trivially valid
		return (True, None)

	increasing = decreasing = (True, None)

	for i in range(1, len(l1)):
		diff = l1[i] - l1[i - 1]

		# Check differences
		if not (1 <= abs(diff) <= 3):
			return (False, i)  # Invalid difference, exit early

		# Check monotonicity
		if diff < 0:
			increasing = False
		elif diff > 0:
			decreasing = False
		else:
			return (False, i) # The list has two consecutive elements of the same value. This is invalid.
		# If neither increasing nor decreasing, exit early
		if not (increasing or decreasing):
			return (False, i)

	return (True, None)  # Both conditions hold


def solve(lines: list[str]) -> int: # Solve function.
	return sum([1 if check_conditions(list(map(lambda x: int(x), line.split(" ")))) else 0 for line in lines])

'''
def check_conditions_skip_one(l1):
	valid, fault_index = check_conditions_fault_index(l1)
	if valid:
		return True

	# Not valid. Try removing that one element and try again.
	print(valid)
	print(fault_index)
	print("feffefefe")
	if fault_index is not None:
		# Remove the current fault-causing element
		if check_conditions(l1[:fault_index] + l1[fault_index+1:]):
			return True

		# Optionally, try removing the previous element
		if fault_index > 0 and check_conditions(l1[:fault_index-1] + l1[fault_index:]):
			return True
	return False
'''

# check_conditions

def check_conditions_skip_one(l1):
	valid = check_conditions(l1)
	if valid:
		return True

	# Not valid. Try removing that one element and try again.
	#print(valid)
	#print(fault_index)
	#print("feffefefe")

	#if fault_index is not None:
	for i in range(len(l1)):
		# Remove the current fault-causing element
		if check_conditions(l1[:i] + l1[i+1:]):
			return True
	return False


def part2(lines: list[str]) -> int:
	# Now just try to do the thing...
	return sum([1 if check_conditions_skip_one(list(map(lambda x: int(x), line.split(" ")))) else 0 for line in lines])

if __name__=="__main__":

	fh = open("input.txt", "r")
	lines = fh.readlines()
	fh.close()
	if PART == 1:
		res = solve(lines)
	elif PART == 2:
		res = part2(lines)
	else:
		print("Invalid part: "+str(PART))
		exit(1)
	print("Result: "+str(res))

		
	exit(0)
