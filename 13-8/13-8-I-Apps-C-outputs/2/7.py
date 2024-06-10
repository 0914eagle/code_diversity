
def get_square_killer_size(memory):
    # Initialize variables
    max_size = 0
    current_size = 0
    row_index = 0
    col_index = 0
    row_count = len(memory)
    col_count = len(memory[0])
    
    # Iterate through the memory matrix
    for i in range(row_count):
        for j in range(col_count):
            # If the current element is 1, check if there is a square killer
            if memory[i][j] == 1:
                # Check if the current element is part of a square killer
                current_size = 1
                for k in range(i, row_count):
                    if memory[k][j] == 1:
                        current_size += 1
                    else:
                        break
                for l in range(j, col_count):
                    if memory[i][l] == 1:
                        current_size += 1
                    else:
                        break
                # Update the maximum size if necessary
                if current_size > max_size:
                    max_size = current_size
    
    # Return the maximum size
    return max_size

def main():
    # Read the input
    row_count, col_count = map(int, input().split())
    memory = []
    for _ in range(row_count):
        memory.append(list(map(int, input())))
    
    # Get the square killer size
    size = get_square_killer_size(memory)
    
    # Print the output
    print(size)

if __name__ == '__main__':
    main()

