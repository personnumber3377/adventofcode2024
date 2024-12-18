

TEST = False

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






def print_spaces(count):
	# Helper function to print spaces
	if count > 0:
		print(' ', end='')
		print_spaces(count - 1)
 
def print_stars(count):
	# Helper function to print stars
	if count > 0:
		print('*', end='')
		print_stars(count - 1)
 
def print_tree_row(spaces, stars):
	# Recursive function to print a row of the Christmas tree
	if spaces > 0:
		print_spaces(spaces)
	if stars > 0:
		print_stars(stars)
	print()  # Move to the next line after printing the row
 
def print_tree(rows, current_row=1):
	# Recursive function to print a single Christmas tree
	if current_row > rows:
		return
	spaces = rows - current_row
	stars = 2 * current_row - 1
	print_tree_row(spaces, stars)
	print_tree(rows, current_row + 1)
 
def print_multiple_trees(num_trees, tree_height):
	# Recursive function to print multiple Christmas trees
	if num_trees == 0:
		return
	print_tree(tree_height)
	print()  # Add an empty line between trees
	print_multiple_trees(num_trees - 1, tree_height)
 
if __name__ == "__main__":
	num_trees = 3  # Number of trees to print
	tree_height = 5  # Height of each tree
 
	# print_multiple_trees(num_trees, tree_height)
	print_tree(51)