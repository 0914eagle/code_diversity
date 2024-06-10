
def get_square_killer(memory):
    # Initialize variables
    max_size = 0
    max_killer = []
    
    # Iterate over each element in the memory
    for i in range(len(memory)):
        for j in range(len(memory[0])):
            # Check if the current element is part of a square killer
            size = check_square_killer(memory, i, j)
            
            # If the size is greater than the current maximum, update the maximum and the maximum killer
            if size > max_size:
                max_size = size
                max_killer = [(i, j)]
                
            # If the size is equal to the current maximum, add the current element to the maximum killer
            elif size == max_size:
                max_killer.append((i, j))
    
    # Return the maximum killer
    return max_killer

def check_square_killer(memory, i, j):
    # Initialize variables
    size = 1
    current = memory[i][j]
    
    # Check if the current element is part of a square killer
    for k in range(i, len(memory)):
        for l in range(j, len(memory[0])):
            # If the element is not part of the killer, return 0
            if memory[k][l] != current:
                return 0
            
            # If the element is part of the killer, update the size and move on to the next element
            size += 1
    
    # If the element is part of a square killer, return the size
    return size

def main():
    # Read the input
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(list(input()))
    
    # Get the largest square killer
    largest_killer = get_square_killer(memory)
    
    # Print the size of the largest square killer
    print(len(largest_killer))

if __name__ == '__main__':
    main()

