
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
	return

if __name__=="__main__":

	test_shortest_numpad()
	test_SHORTEST_PATHS_NUMPAD_KEYS()

	exit(0)
