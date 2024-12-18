
import re
import sys
import copy

TEST = False
PART = 1


def go_forward_in_time(p0, v, t): # This function returns the position after t timesteps.
	# Basically just p = p0 + v*t
	assert isinstance(t, int) # Timestep should be discrete integer.
	return (p0[0] + v[0]*t, p0[1] + v[1]*t)

if TEST:
	MAP_HEIGHT = 7
	MAP_WIDTH = 11

	MAP_WIDTH_MIDDLE = 4
	MAP_HEIGHT_MIDDLE = 3

else:
	MAP_HEIGHT = 103
	MAP_WIDTH = 101

	MAP_WIDTH_MIDDLE = 50
	MAP_HEIGHT_MIDDLE = 51

def generate_tree_set() -> set:
	out = set()
	for i in range(MAP_HEIGHT-1):
		for k in range(i):
			return


# Generate the tree set

TREE_SET = generate_tree_set()


MIDDLE_CROSS = 0 # This is when we are in the boundary between quadrants. These do not count towards the total score.
BOTTOM_RIGHT = 1
BOTTOM_LEFT = 2
TOP_RIGHT = 3
TOP_LEFT = 4
TIMESTEPS = 100

def clamp_positions(positions):
	# So the position is basically just (x % width, y % height)
	return [(x[0] % MAP_WIDTH, x[1] % MAP_HEIGHT) for x in positions]

def quadrant(position): # Returns the quadrant thing. 0 means that it is in the middle cross which doesn't accumulate score.
	x = position[0]
	y = position[1]
	if x > MAP_WIDTH_MIDDLE: # On the right side.
		if y > MAP_HEIGHT_MIDDLE:
			# Bottom right.
			return BOTTOM_RIGHT
		elif y < MAP_HEIGHT_MIDDLE: # We can not just use else because if we are in the middle, then that doesn't count.
			# Top right
			return TOP_RIGHT
		else: # Boundary.
			return MIDDLE_CROSS
	elif x < MAP_WIDTH_MIDDLE:
		if y > MAP_HEIGHT_MIDDLE:
			# Bottom left.
			return BOTTOM_LEFT
		elif y < MAP_HEIGHT_MIDDLE: # We can not just use else because if we are in the middle, then that doesn't count.
			# Top left
			return TOP_LEFT
		else: # Boundary.
			return MIDDLE_CROSS
	else: # On the boundary
		return MIDDLE_CROSS
	assert False

def calc_safety_score(positions):
	quadrant_buckets = [0,0,0,0,0] # The first one is basically the cross boundary so it doesn't count towards the total.
	for pos in positions:
		q = quadrant(pos)
		assert q in list(range(5))
		quadrant_buckets[q] += 1
	#print("Our quadrant buckets:"+str(quadrant_buckets))
	assert sum(quadrant_buckets) <= len(positions) # Can not be more marks in the quadrant buckets than there are positions.

	return quadrant_buckets[1]*quadrant_buckets[2]*quadrant_buckets[3]*quadrant_buckets[4]

def render_matrix(matrix):
	#print(matrix)
	print("="*30)
	for line in matrix:
		for char in line:
			if char != 0:
				assert char < 10 # If more than ten then this fucks up the showing.
				print(str(char), end="")
			else:
				print(".", end="")
		print("\n", end="")
	print("="*30)
	return

def go_forward_and_clamp(drones, t):
	new_positions = [[go_forward_in_time(x[0], x[1], t), x[1]] for x in drones] # Go forward in time.
	clamped_positions = clamp_positions([x[0] for x in new_positions]) # This basically figures out where in the box we should actually be. Basically does modular arithmetic to figure out which space we actually loop back around to.
	return clamped_positions


def show_positions(positions): # This takes in the clamped positions...
	show_matrix = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

	# Now just put all of the stuff.
	for pos in positions:
		show_matrix[pos[1]][pos[0]] += 1

	render_matrix(show_matrix)

	return

def render_drones(drones):
	# Shows all of the timesteps.
	new_positions = copy.deepcopy(drones)
	for i in range(TIMESTEPS):
		print("T = "+str(i))
		new_positions = [[go_forward_in_time(x[0], x[1], 1), x[1]] for x in new_positions] # Go forward in time.
		clamped_positions = clamp_positions([x[0] for x in new_positions]) # This basically figures out where in the box we should actually be. Basically does modular arithmetic to figure out which space we actually loop back around to.

		show_positions(clamped_positions)

	return

def simulate_drones(drone_strings):
	# First parse

	drones = [] # A list of lists of tuples. each element is [(p0_x, p0_y), (vx, xy)]
	for string in drone_strings:
		p_str, v_str = string.split(" ")
		p_str = p_str[2:] # Cut out "p="
		v_str = v_str[2:] # Cut out "v="
		p_x, p_y = [int(x) for x in p_str.split(",")]
		v_x, v_y = [int(x) for x in v_str.split(",")]
		drones.append([(p_x, p_y), (v_x, v_y)])

	if TEST:
		render_drones(copy.deepcopy(drones))

	new_positions = [go_forward_in_time(x[0], x[1], TIMESTEPS) for x in drones] # Go forward in time.
	clamped_positions = clamp_positions(new_positions) # This basically figures out where in the box we should actually be. Basically does modular arithmetic to figure out which space we actually loop back around to.

	# Calculate safety score:
	if TEST:
		print("Our shit:")
		show_positions(clamped_positions)
	safety_score = calc_safety_score(clamped_positions)

	return safety_score


def check_for_tree(positions) -> bool:
	# Check for the hardcodede thing.

def simulate_drones_tree(drone_strings):
	# First parse

	drones = [] # A list of lists of tuples. each element is [(p0_x, p0_y), (vx, xy)]
	for string in drone_strings:
		p_str, v_str = string.split(" ")
		p_str = p_str[2:] # Cut out "p="
		v_str = v_str[2:] # Cut out "v="
		p_x, p_y = [int(x) for x in p_str.split(",")]
		v_x, v_y = [int(x) for x in v_str.split(",")]
		drones.append([(p_x, p_y), (v_x, v_y)])


	# Loop until we find a tree.

	# We assume that the tree is like as follows:

	#######
	#  X  #
	# XXX #
	#XXXXX#
	#  X  #
	#######

	time_count = 0 # Time steps.

	while True:

		new_positions = [go_forward_in_time(x[0], x[1], 1) for x in drones] # Go forward in time.
		clamped_positions = clamp_positions(new_positions) # This basically figures out where in the box we should actually be. Basically does modular arithmetic to figure out which space we actually loop back around to.
		time_count += 1 # We advanced once.

		# Now check for the tree.

		if check_for_tree(clamped_positions):
			return time_count



	assert False



def solve() -> int:
	
	if len(sys.argv) != 2:
		print("Usage: python "+str(sys.argv[0])+" INPUTFILE")
		return 1

	fh = open(sys.argv[1], "r")
	lines = fh.readlines()
	fh.close()
	if PART==1:

		sol = simulate_drones(lines)
		print("Solution to part one: "+str(sol))
	elif PART==2:
		sol = simulate_drones_tree(lines)
		print("Solution to part two: "+str(sol))
	else:
		print("Invalid part: "+str(PART))
		return 1
	return 0

if __name__=="__main__":

	ret = solve()

	exit(ret)
