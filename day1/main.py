
PART = 2

def part1(lines: list[str]) -> int: # Solve function.
	nums1 = []
	nums2 = []
	for string in lines:
		num1, num2 = string.split("   ")
		nums1.append(int(num1))
		nums2.append(int(num2))

	nums1.sort()
	nums2.sort()

	diffs = [abs(x[0] - x[1]) for x in zip(nums1,nums2)]
	return sum(diffs)

def count_nums(nums) -> dict: # This generates a dictionary with number as key and how many occurences as value.
	o = {}
	for num in nums:
		if num not in o:
			o[num] = 1
		else:
			o[num] += 1
	return o

def calculate_similarity_score(nums1, nums2) -> int:
	count1, count2 = count_nums(nums1), count_nums(nums2)
	# print(count1)
	# print(count2)
	mult_list = [count1[key]*count2[key]*key if key in count2 else 0 for key in count1.keys()]
	# print(mult_list)
	return sum(mult_list) # No need to check the other way, because numbers which are only in count2 don't count towards the total anyway.

def part2(lines: list[str]) -> int: # Solve function.
	nums1 = []
	nums2 = []
	for string in lines:
		num1, num2 = string.split("   ")
		nums1.append(int(num1))
		nums2.append(int(num2))

	out = calculate_similarity_score(nums1, nums2)

	return out

if __name__=="__main__":

	fh = open("input.txt", "r")
	lines = fh.readlines()
	fh.close()
	if PART == 1:
		res = part1(lines)
	elif PART == 2:
		res = part2(lines)
	else:
		print("Invalid part: "+str(PART))
		exit(1)
	print("Result: "+str(res))

		
	exit(0)
