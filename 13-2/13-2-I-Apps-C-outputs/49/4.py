
def solve_bar_code(n, vertical_spec, horizontal_spec):
    # Initialize the solution matrix
    solution = [[0] * (n+1) for _ in range(n)]

    # Iterate through the vertical specification
    for i, spec in enumerate(vertical_spec):
        # Find the number of groups to form
        num_groups = len(spec)

        # Iterate through the groups
        for j, group_size in enumerate(spec):
            # Find the starting index of the group
            start_index = j * group_size

            # Mark the borders in the group
            for k in range(start_index, start_index + group_size):
                solution[i][k] = 1

    # Iterate through the horizontal specification
    for j, spec in enumerate(horizontal_spec):
        # Find the number of groups to form
        num_groups = len(spec)

        # Iterate through the groups
        for i, group_size in enumerate(spec):
            # Find the starting index of the group
            start_index = i * group_size

            # Mark the borders in the group
            for k in range(start_index, start_index + group_size):
                solution[k][j] = 1

    # Return the solution matrix
    return solution

