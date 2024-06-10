
def find_largest_square_killer(memory):
    # Initialize variables
    largest_killer_size = 0
    current_killer_size = 0
    killer_found = False
    
    # Iterate through the memory matrix
    for row in range(len(memory)):
        for col in range(len(memory[0])):
            # If the current cell is a part of a killer, increment the current killer size
            if memory[row][col] == '1':
                current_killer_size += 1
            # If the current cell is not a part of a killer, check if the current killer size is larger than the largest killer size
            elif current_killer_size > largest_killer_size:
                largest_killer_size = current_killer_size
                current_killer_size = 0
    
    # If a killer was found, return its size. Otherwise, return -1.
    if largest_killer_size > 0:
        return largest_killer_size
    else:
        return -1

def main():
    # Read the input
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(input())
    
    # Find the largest square killer
    largest_killer_size = find_largest_square_killer(memory)
    
    # Print the output
    print(largest_killer_size)

if __name__ == '__main__':
    main()

