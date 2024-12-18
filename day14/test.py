
from day14 import * # Import the solution which to test.

import random

MIN_POS_X = 0
MAX_POS_X = MAP_WIDTH

MIN_POS_Y = 0
MAX_POS_Y = MAP_HEIGHT




MIN_VEL_X = -100
MAX_VEL_X = 100

MIN_VEL_Y = -100
MAX_VEL_Y = 100


TEST_COUNT = 1000

TIMESTEPS = 100

def test_clamp():
	for i in range(TEST_COUNT):
		# Generate random drone.
		rand_drone_thing = [[(random.randrange(MIN_POS_X, MAX_POS_X), random.randrange(MIN_POS_Y, MAX_POS_Y)), (random.randrange(MIN_VEL_X, MAX_VEL_X), random.randrange(MIN_VEL_Y, MAX_VEL_Y))]]

		# Now see if the thing differs
		# First get the result of a one go thing.
		one_go_res = go_forward_and_clamp(rand_drone_thing, TIMESTEPS)[0]
		one_go_res = [one_go_res, rand_drone_thing[0][1]]
		# Go one step at a time.
		cur_pos = rand_drone_thing[0][0]
		for i in range(TIMESTEPS):
			cur_pos = go_forward_and_clamp([[cur_pos, rand_drone_thing[0][1]]], 1)[0]

		# Now check to see any difference.
		if [cur_pos, rand_drone_thing[0][1]] != one_go_res:
			print("Found discrepency with these parameters:")
			print("p0: "+str(rand_drone_thing[0][0]))
			print("v: "+str(rand_drone_thing[0][1]))
			print("One go thing: "+str(one_go_res))
			print("Incremental: "+str([cur_pos, rand_drone_thing[0][1]]))
			assert False
		print("Passed one test case!")
	print("Passed!")
	return


if __name__=="__main__":
	test_clamp()
	exit(0)