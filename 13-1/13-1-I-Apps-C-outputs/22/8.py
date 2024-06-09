
def solve_bar_code(n, vertical_spec, horizontal_spec):
    # Initialize the solution matrix
    solution = [[0] * (n+1) for _ in range(n)]

    # Iterate through the vertical specification
    for i, spec in enumerate(vertical_spec):
        # Find the number of groups to form
        num_groups = len(spec)

        # Iterate through the groups
        for j in range(num_groups):
            # Find the length of the current group
            group_length = spec[j]

            # Mark the corresponding borders as 1
            for k in range(group_length):
                solution[i][j*group_length + k] = 1

    # Iterate through the horizontal specification
    for j, spec in enumerate(horizontal_spec):
        # Find the number of groups to form
        num_groups = len(spec)

        # Iterate through the groups
        for i in range(num_groups):
            # Find the length of the current group
            group_length = spec[i]

            # Mark the corresponding borders as 1
            for k in range(group_length):
                solution[i*group_length + k][j] = 1

    return solution

