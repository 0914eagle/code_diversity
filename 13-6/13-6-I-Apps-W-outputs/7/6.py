
def solve(n, path):
    # Initialize a list to store the path
    path_list = [1]

    # Iterate through the path
    for i in range(1, n):
        # Get the index of the router to connect to
        connect_to = path[i-1]

        # Check if the router has already been visited
        if connect_to in path_list:
            # If it has, return an empty list to indicate an invalid path
            return []

        # Add the router to the path
        path_list.append(connect_to)

    # Return the path list
    return path_list

