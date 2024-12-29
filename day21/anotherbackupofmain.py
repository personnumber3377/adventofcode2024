
# Dictionary which maps the moves and initial positions to end positions, if the move is not in this dictionary, then it is invalid: "In particular, if a robot arm is ever aimed at a gap where no button is present on the keypad, even for an instant, the robot will panic unrecoverably."

# KEYPAD_MOVES = {}

from shortest_grids import *
from constants import *

SHORTEST_PATHS_NUMPAD = generate_shortest_paths_numpad()
SHORTEST_PATHS_ARROWPAD = generate_shortest_paths_arrowpad()



# Now these functions are used to get the shortest paths from a position to another.

def generate_shortest_paths_arrowpad_keys():
	
	out = dict() # Generate the dictionary

	all_keys = ARROWPAD.keys() # Get the keys.
	for start_key in all_keys:
		for end_key in all_keys:
			if start_key == end_key:
				continue
			start_pos = ARROWPAD[start_key]
			end_pos = ARROWPAD[end_key]
			# res[(start[0], start[1], end[0], end[1])]
			out[(start_key, end_key)] = SHORTEST_PATHS_ARROWPAD[(start_pos[0], start_pos[1], end_pos[0], end_pos[1])]
	return out

def generate_shortest_paths_numpad_keys():
	out = dict() # Generate the dictionary

	all_keys = NUMPAD.keys() # Get the keys.
	for start_key in all_keys:
		for end_key in all_keys:
			if start_key == end_key:
				continue
			start_pos = NUMPAD[start_key]
			end_pos = NUMPAD[end_key]
			# res[(start[0], start[1], end[0], end[1])]
			out[(start_key, end_key)] = SHORTEST_PATHS_NUMPAD[(start_pos[0], start_pos[1], end_pos[0], end_pos[1])]
	return out






SHORTEST_PATHS_NUMPAD_KEYS = generate_shortest_paths_numpad_keys()
SHORTEST_PATHS_ARROWPAD_KEYS = generate_shortest_paths_arrowpad_keys()




def check_valid_numpad(x,y):
	# Checks if the position is valid in 
	return


# Just do the thing...

'''

+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

'''


# SHORTEST_PATHS_ARROWPAD_INPUT_KEYS
# These are basically the shortest ways to input a character to the second arrowpad from the first. The key is the wanted character and the value is the input into the original arrowpad:

SHORTEST_PATHS_ARROWPAD_INPUT_KEYS =   {"<": "<v<A",
										"^": "<A",
										"v": "<vA",
										">": "vA"}


'''

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

'''


def keypad_forward(actions, init_pos): # Init pos is the tuple
	assert actions[-1] == "A" # No point in moving if we don't press A, this means that there is a bug somewhere.
	# Applies the actions "actions" to the nine digit display and returns the results...

	# First split on the A button presses.

	press_actions = actions.split("A")


	# This is the location of the "A" character in the numpad.
	x = 2
	y = 3

	for action_seq in press_actions:
		for c in action_seq:
			match c:
				case "<":
					x -= 1
				case ">":
					x += 1

def get_shortest_path(code) -> str: # Generates the shortest path which types this code.
	cache = dict() # This is to memoieze the shortest shit such that we do not need to compute it every time.
	# Initialize the positions of every "pointer"
	keypad_pos = (2,3) # Pointing at "A"
	# Both of the arrowpads
	arrowpad1_pos = (2,0)
	arrowpad2_pos = (2,0)

	# Now generate all of the code changes.

	cur_shortest_path = "" # Current shortest path
	cur_shortest_path_len = 10**9 # Some very big number such that we initialize on the first loop iteration.
	for i in range(len(code)-1):
		start_key = code[i]
		end_key = code[i+1]
		if start_key != "A":
			start_key = int(start_key)
		if end_key != "A":
			end_key = int(end_key)
		print("from : to == "+str(start_key)+", "+str(end_key))
		# First generate all of the shortest paths in the initial keypad.
		numpad_paths = SHORTEST_PATHS_NUMPAD_KEYS[(start_key, end_key)]
		# Now iterate over those paths...
		for path1 in numpad_paths:
			print("path1 == "+str(path1))
			# Now the path variable contains the suspected shortest path in the original keypad.
			# Now we need to iterate over the other bullshit paths...
			# The arrowpad shit is in the SHORTEST_PATHS_ARROWPAD_KEYS
			# So now just do the bullshit again but with the other bullshit maybe???
			for j in range(len(path1)-1): # Basically do the same algorithm as above but "one layer down"
				start2_key = path1[j]
				end2_key = path1[j+1]
				if start2_key == end2_key:
					continue
				print("(start2_key, end2_key) == "+str((start2_key, end2_key)))

				assert (start2_key, end2_key) in SHORTEST_PATHS_ARROWPAD_KEYS
				arrowpad_paths = SHORTEST_PATHS_ARROWPAD_KEYS[(start2_key, end2_key)] # Get the shortest shit...
				for path2 in arrowpad_paths:
					print("path2 == "+str(path2))
					for k in range(len(path2)):
						start3_key = path2[k]
						#end3_key = path2[i+1]
						print("FUCKFUCKFCUK")
						#if start3_key == end3_key:
						#	continue
						print("FUCKFUCKFCUK")
						#assert (start3_key, end3_key) in SHORTEST_PATHS_ARROWPAD_INPUT_KEYS
						arrowpad_paths2 = SHORTEST_PATHS_ARROWPAD_INPUT_KEYS[start3_key] # Get the shortest shit...
						for path3 in arrowpad_paths2:
							# Ok, so now the path is path1 in the numpad path2 in the first arrowpad and path3 in the second arrowpad.
							# The total path is therefore path1+path2+path3
							total_path = path1+path2+path3
							print("Here is the current path: "+str(total_path))
							if len(total_path) < cur_shortest_path_len:
								cur_shortest_path_len = len(total_path)
								cur_shortest_path = total_path
	print("Shortest path: "+str(cur_shortest_path))


	exit(1)


def solve(lines: list[str]) -> int: # Solve function.
	'''

	The length of the shortest sequence of button presses you need to type on your directional keypad in order to cause the code to be typed on the numeric keypad; for 029A, this would be 68.
	The numeric part of the code (ignoring leading zeroes); for 029A, this would be 29.

	'''

	output = 0
	for code in lines:
		print("code == "+str(code))
		code = code[:-1]
		assert code[-1] == "A"

		shortest_path = get_shortest_path(code)
		# Now just convert the numeric thing and then multiply with the length
		numeric_part_of_code = code[:-1] # Cut out "A"
		numeric_part_of_code = int(numeric_part_of_code)
		# Now just multiply and add to total.
		output += len(shortest_path)*numeric_part_of_code
	return output


if __name__=="__main__":

	fh = open("input.txt", "r")
	lines = fh.readlines()
	fh.close()

	res = solve(lines)

	print("Result: "+str(res))

		
	exit(0)
