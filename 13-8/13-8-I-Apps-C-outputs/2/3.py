
def get_largest_square_killer(memory):
    # Initialize variables
    largest_killer_size = 0
    current_killer_size = 0
    killer_found = False
    
    # Iterate through the memory matrix
    for row in range(len(memory)):
        for col in range(len(memory[0])):
            # Check if the current cell is part of a killer
            if memory[row][col] == '1':
                current_killer_size += 1
                # Check if the current killer is larger than the largest killer found so far
                if current_killer_size > largest_killer_size:
                    largest_killer_size = current_killer_size
            # Check if the current cell is not part of a killer
            else:
                current_killer_size = 0
    
    # Return the largest killer size
    return largest_killer_size

def main():
    # Read the input
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(input())
    
    # Get the largest square killer
    largest_killer_size = get_largest_square_killer(memory)
    
    # Print the output
    print(largest_killer_size)

if __name__ == '__main__':
    main()

