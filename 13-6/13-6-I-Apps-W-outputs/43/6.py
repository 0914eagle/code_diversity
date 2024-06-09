
def get_mappings(maze, s):
    # Initialize a list to store the mappings
    mappings = []
    
    # Loop through each digit in the instructions
    for i in range(len(s)):
        # Get the current digit and the next digit
        current_digit = s[i]
        next_digit = s[i+1] if i < len(s)-1 else -1
        
        # Check if the current digit is a valid direction
        if current_digit in ["0", "1", "2", "3"]:
            # Check if the next digit is a valid direction
            if next_digit in ["0", "1", "2", "3"]:
                # Check if the current digit is not the same as the next digit
                if current_digit != next_digit:
                    # Add the current digit and the next digit to the mappings
                    mappings.append((current_digit, next_digit))
    
    # Return the mappings
    return mappings

def get_exit_mappings(maze, s):
    # Get the mappings for the instructions
    mappings = get_mappings(maze, s)
    
    # Initialize a set to store the unique mappings
    unique_mappings = set()
    
    # Loop through each mapping
    for mapping in mappings:
        # Check if the mapping is already in the unique mappings
        if mapping not in unique_mappings:
            # Add the mapping to the unique mappings
            unique_mappings.add(mapping)
    
    # Return the number of unique mappings
    return len(unique_mappings)

def main():
    # Read the input
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    s = input()
    
    # Get the number of mappings that lead to the exit
    result = get_exit_mappings(maze, s)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

