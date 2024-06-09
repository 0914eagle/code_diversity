
def get_maze_size(maze):
    return (len(maze), len(maze[0]))

def get_joe_location(maze):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == "J":
                return (r, c)
    return None

def get_fire_locations(maze):
    fire_locations = []
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == "F":
                fire_locations.append((r, c))
    return fire_locations

def is_safe_to_exit(maze, joe_location, fire_locations):
    (r, c) = joe_location
    for (fr, fc) in fire_locations:
        if r == fr or c == fc:
            return False
    return True

def get_fastest_exit_time(maze, joe_location, fire_locations):
    (r, c) = joe_location
    (rows, cols) = get_maze_size(maze)
    fastest_time = float("inf")
    for (fr, fc) in fire_locations:
        distance = abs(r - fr) + abs(c - fc)
        if distance < fastest_time:
            fastest_time = distance
    return fastest_time

def solve_maze(maze):
    joe_location = get_joe_location(maze)
    fire_locations = get_fire_locations(maze)
    if is_safe_to_exit(maze, joe_location, fire_locations):
        return "IMPOSSIBLE"
    else:
        return get_fastest_exit_time(maze, joe_location, fire_locations)

if __name__ == '__main__':
    maze = [
        "####",
        "#JF#",
        "#..#",
        "#..#"
    ]
    print(solve_maze(maze))

