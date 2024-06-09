
def solve(memory):
    # Initialize variables
    max_size = 0
    max_killer = []

    # Loop through each row of the memory
    for i in range(len(memory)):
        # Loop through each column of the memory
        for j in range(len(memory[0])):
            # Check if the current cell is part of a killer
            if memory[i][j] == "1":
                # Find the size of the killer
                size = find_killer_size(memory, i, j)

                # If the killer is larger than the current largest killer, update the variables
                if size > max_size:
                    max_size = size
                    max_killer = [[i, j]]

                # If the killer is the same size as the current largest killer, add it to the list of killers
                elif size == max_size:
                    max_killer.append([i, j])

    # Return the size of the largest killer
    return max_size

# Find the size of a killer starting at a given cell
def find_killer_size(memory, i, j):
    # Initialize variables
    size = 0
    visited = set()

    # Loop through each cell in the killer
    for di in range(-size, size+1):
        for dj in range(-size, size+1):
            # Check if the current cell is part of the killer
            if memory[i+di][j+dj] == "1" and (i+di, j+dj) not in visited:
                # Add the current cell to the visited set
                visited.add((i+di, j+dj))

                # Increment the size of the killer
                size += 1

    # Return the size of the killer
    return size

