
from shortest_grids import *
from main import *



def test_shortest_numpad():
	res = generate_shortest_paths_numpad()
	print(res)
	# Now let's check the shortest paths from "A" to "7"
	start = NUMPAD["A"]
	end = NUMPAD[7]
	# Now check the result:
	print("Shortest paths from A to 7: "+str(res[(start[0], start[1], end[0], end[1])]))
	return

def test_SHORTEST_PATHS_NUMPAD_KEYS():
	print("Here are the shortest paths on the numpad:")
	print(SHORTEST_PATHS_NUMPAD_KEYS)
	print("Here is the path from A to 7:")
	print(SHORTEST_PATHS_NUMPAD_KEYS[("A", 7)])
	print("Here is the path from A to 0:")
	print(SHORTEST_PATHS_NUMPAD_KEYS[("A", 0)])
	return

def test_bfs_shortest_paths():
	# Example test

	grid = [[0,0,0],
			[0,0,0],
			[0,0,0],
			[1,0,0]]

	start_pos = (2,3)
	end_pos = (1,3)
	print("Here is the bullshit:")
	res = bfs_shortest_paths(grid, start_pos, end_pos)
	print(res)
	assert res != [] # Should be a path.
	return

if __name__=="__main__":

	test_shortest_numpad()
	test_SHORTEST_PATHS_NUMPAD_KEYS()
	test_bfs_shortest_paths()

	exit(0)
