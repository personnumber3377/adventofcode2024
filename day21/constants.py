'''

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
			out[(start_key, end_key)] = SHORTEST_PATHS_NUMPAD[(start[0], start[1], end[0], end[1])]
	return out

'''

NUMPAD = {
	0: (1, 3),
	1: (0, 2), 2: (1, 2), 3: (2, 2),
	4: (0, 1), 5: (1, 1), 6: (2, 1),
	7: (0, 0), 8: (1, 0), 9: (2, 0), "A": (2, 3)
}


# Possible moves and their offsets
MOVES = {
	"^": (0, -1),
	"v": (0, 1),
	"<": (-1, 0),
	">": (1, 0),
	"A": (0, 0)
}

# Reverse lookup for moves
MOVE_KEYS = {v: k for k, v in MOVES.items()}

'''

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

'''

ARROWPAD = {
	"<": (0,1),
	">": (2,1),
	"^": (1,0),
	"v": (1,1),
	"A": (2,0)
}
