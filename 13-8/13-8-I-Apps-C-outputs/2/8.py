
def find_square_killers(memory):
    # Initialize variables
    largest_killer_size = 0
    killer_size = 0
    killer_present = False
    
    # Loop through each row of the memory
    for row in range(len(memory)):
        # Loop through each column of the memory
        for col in range(len(memory[0])):
            # If the current position is a 1, check if there is a killer present
            if memory[row][col] == "1":
                # Check if there is a killer present in the current position
                killer_present = check_killer(memory, row, col)
                
                # If a killer is present, update the largest killer size
                if killer_present:
                    largest_killer_size = max(largest_killer_size, killer_size)
                    
    # Return the largest killer size
    return largest_killer_size

def check_killer(memory, row, col):
    # Initialize variables
    global killer_size
    killer_size = 0
    killer_present = False
    
    # Check if the current position is a 1
    if memory[row][col] == "1":
        # Check if there is a killer present in the current position
        killer_present = check_killer_helper(memory, row, col, 1)
    
    # Return whether a killer is present
    return killer_present

def check_killer_helper(memory, row, col, size):
    # Base case: If the size is greater than the largest killer size, return False
    if size > largest_killer_size:
        return False
    
    # Base case: If the current position is not a 1, return False
    if memory[row][col] != "1":
        return False
    
    # Recursive case: If the current position is a 1, check if there is a killer present in the next position
    killer_present = check_killer_helper(memory, row, col + 1, size + 1)
    
    # If a killer is present, update the killer size and return True
    if killer_present:
        killer_size = size
        return True
    
    # Recursive case: If a killer is not present in the next position, check if there is a killer present in the next row
    return check_killer_helper(memory, row + 1, col, 1)

def main():
    # Read input from stdin
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(input())
    
    # Find the largest square killer
    largest_killer_size = find_square_killers(memory)
    
    # Print the largest square killer size
    print(largest_killer_size)

if __name__ == '__main__':
    main()

