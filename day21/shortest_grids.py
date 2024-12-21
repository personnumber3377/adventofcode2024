


from collections import deque
# from main import *
from constants import *

def is_valid(x, y, grid, visited):
    """Check if a position is valid for movement."""
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and (x, y) not in visited

def bfs_shortest_paths(grid, start, end):
    """Find all shortest paths from start to end on a 2D grid."""
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
    queue = deque([(start, [start])])  # (current_position, path_so_far)
    visited = set()
    shortest_distance = float('inf')
    all_paths = []

    while queue:
        (x, y), path = queue.popleft()

        # Stop exploring if we go beyond the shortest known distance
        if len(path) > shortest_distance:
            continue

        # Reached the destination
        if (x, y) == end:
            if len(path) < shortest_distance:
                shortest_distance = len(path)
                all_paths = [path]  # Reset paths for a new shorter distance
            elif len(path) == shortest_distance:
                all_paths.append(path)
            continue

        # Mark as visited
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid, visited):
                queue.append(((nx, ny), path + [(nx, ny)]))

    return all_paths

def path_to_string(path) -> str: # This bullshit returns the string which corresponds to the bullshit thing...
    start = path[0]
    path.pop(0)
    out = ""
    for elem in path:
        move_shit = (elem[0] - start[0], elem[1] - start[1])
        start = elem
        assert move_shit in MOVE_KEYS
        thing = MOVE_KEYS[move_shit]
        assert isinstance(thing, str)
        out += thing
    return out

def generate_shortest_paths_numpad():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0]
    ]

    output = dict()
    banned = (0,3) # This is the banned space
    for x1 in range(0,3):
        for y1 in range(0,4):
            # (x,y) is the start
            start = (x1,y1)
            for x2 in range(0,3):
                for y2 in range(0,4):
                    end = (x2,y2)
                    if start == end:
                        continue
                    if start == banned or end == banned:
                        continue
                    paths = [path_to_string(x) for x in bfs_shortest_paths(grid, start, end)]
                    assert (x1,y1,x2,y2) not in output
                    output[(x1,y1,x2,y2)] = paths # Just add it like this?????

    return output

def generate_shortest_paths_arrowpad():
    # This one is for the robot control stuff.
    grid = [
        [1, 0, 0],
        [0, 0, 0]
    ]

    output = dict()
    banned = (0,0) # This is the banned space
    for x1 in range(0,3):
        for y1 in range(0,2):
            # (x,y) is the start
            start = (x1,y1)
            for x2 in range(0,3):
                for y2 in range(0,2):
                    end = (x2,y2)
                    if start == end:
                        continue
                    if start == banned or end == banned:
                        continue
                    paths = [path_to_string(x) for x in bfs_shortest_paths(grid, start, end)]
                    assert (x1,y1,x2,y2) not in output
                    output[(x1,y1,x2,y2)] = paths # Just add it like this?????

    return output



# Example Usage
if __name__ == "__main__":
    # Define a grid (0 = open, 1 = occupied)
    grid = [
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]
    start = (0, 0)
    end = (2, 3)
    paths = bfs_shortest_paths(grid, start, end)
    print("All shortest paths:")
    for path in paths:
        print(path)
