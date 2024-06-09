
def can_grasshopper_eat_insect(n, k, line):
    # Initialize variables
    start_index = line.index("G")
    end_index = line.index("T")
    jumps = 0

    # Loop through the line and check if the grasshopper can jump to the end index
    for i in range(start_index, end_index):
        if line[i] == ".":
            jumps += 1
            if jumps == k:
                return True
        else:
            jumps = 0

    # If the grasshopper reached the end index, return True
    if jumps == k:
        return True

    # Otherwise, return False
    return False

