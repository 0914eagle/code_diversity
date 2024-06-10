
def get_largest_square_killer(memory):
    # Initialize variables
    largest_killer = 0
    killer_size = 0
    killer_found = False

    # Iterate over the memory matrix
    for row in range(len(memory)):
        for col in range(len(memory[0])):
            # If the current element is a killer, update the largest killer size
            if is_killer(memory, row, col, killer_size):
                largest_killer = killer_size
                killer_found = True
            # If the current element is not a killer, update the killer size
            else:
                killer_size = 0

    # If no killer was found, return -1
    if not killer_found:
        return -1

    # Return the largest killer size
    return largest_killer

def is_killer(memory, row, col, killer_size):
    # If the current element is not a 1, it cannot be a killer
    if memory[row][col] != "1":
        return False

    # If the killer size is 0, it means this is the first element of the killer
    if killer_size == 0:
        killer_size = 1

    # Check if the killer is still valid in the current row and column
    if is_killer_valid(memory, row, col, killer_size):
        return True

    # If the killer is not valid, return False
    return False

def is_killer_valid(memory, row, col, killer_size):
    # Check if the killer is valid in the current row
    for i in range(col, col + killer_size):
        if memory[row][i] != "1":
            return False

    # Check if the killer is valid in the current column
    for i in range(row, row + killer_size):
        if memory[i][col] != "1":
            return False

    # If the killer is valid in both the current row and column, return True
    return True

if __name__ == '__main__':
    # Read the input
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(list(input()))

    # Get the largest square killer
    largest_killer = get_largest_square_killer(memory)

    # Print the output
    print(largest_killer)

