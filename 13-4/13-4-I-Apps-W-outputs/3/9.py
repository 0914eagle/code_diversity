
def solve(n, line, order):
    # Convert the input to a list of integers
    line = [int(i) for i in line.split()]
    order = [int(i) for i in order.split()]

    # Check if the input is valid
    if len(line) != n or len(order) != n:
        return "Invalid input"

    # Initialize a variable to keep track of the number of rotations
    rotations = 0

    # Loop through the line of breads
    for i in range(n):
        # Check if the current bread is in the correct position
        if line[i] != order[i]:
            # Find the index of the correct bread in the line
            correct_index = order.index(line[i])

            # Rotate the subsequence of breads to the right
            line = line[:i] + line[i+1:correct_index+1] + [line[i]] + line[correct_index+1:i] + line[i+1:]

            # Increment the number of rotations
            rotations += 1

    # Check if the line of breads is sorted in the correct order
    if line == order:
        return "Possible"
    else:
        return "Impossible"

