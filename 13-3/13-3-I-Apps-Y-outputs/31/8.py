
def get_optimized_path(path):
    # Initialize variables
    optimized_path = path
    endpoint = path[-1]
    min_substring_length = len(path)
    start_index, end_index = 0, 0

    # Iterate through the path
    for i in range(len(path)):
        # Check if the substring starting from index i is a valid substring
        if is_valid_substring(path, i):
            # Check if the substring is shorter than the current minimum length
            if len(path[i:]) < min_substring_length:
                # Update the minimum length and the start and end indices
                min_substring_length = len(path[i:])
                start_index = i
                end_index = i + min_substring_length - 1

    # Check if a substring was found
    if min_substring_length < len(path):
        # Remove the substring from the path
        optimized_path = path[:start_index] + path[end_index + 1:]

    # Return the optimized path
    return optimized_path

def is_valid_substring(path, start_index):
    # Initialize variables
    substring = path[start_index:]
    endpoint = substring[-1]

    # Check if the substring is not empty
    if len(substring) == 0:
        return False

    # Check if the substring ends at the same point as the original path
    if endpoint != path[-1]:
        return False

    # Check if the substring is a valid path
    if not is_valid_path(substring):
        return False

    # The substring is valid
    return True

def is_valid_path(path):
    # Initialize variables
    x, y = 0, 0
    valid_moves = ["L", "R", "U", "D"]

    # Iterate through the path
    for move in path:
        # Check if the move is valid
        if move not in valid_moves:
            return False

        # Update the coordinates based on the move
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "U":
            y += 1
        elif move == "D":
            y -= 1

    # The path is valid
    return True

if __name__ == '__main__':
    # Read the input
    t = int(input())
    paths = []
    for i in range(t):
        n = int(input())
        path = input()
        paths.append(path)

    # Optimize the paths
    optimized_paths = []
    for path in paths:
        optimized_path = get_optimized_path(path)
        optimized_paths.append(optimized_path)

    # Print the results
    for optimized_path in optimized_paths:
        if optimized_path == "-1":
            print("-1")
        else:
            print(optimized_path)

