
def can_reach_n(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Set the first and last cells to 1, as they belong to wooden platforms
    a[0] = a[n + 1] = 1
    
    # Iterate through the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Iterate through the cells of the current platform
        for j in range(length):
            # Set the cell to the index of the current platform
            a[i + j + 1] = i + 1
    
    # Initialize the maximum distance of jump as d
    max_distance = d
    
    # Initialize the current position as 0
    current_position = 0
    
    # Initialize the sequence of jumps as empty
    sequence = []
    
    # Iterate until the current position is n + 1
    while current_position < n + 1:
        # Check if the current position belongs to a wooden platform
        if a[current_position] != 0:
            # Get the index of the wooden platform
            platform = a[current_position]
            
            # Check if the platform is not the last platform
            if platform != m:
                # Get the length of the next platform
                next_platform_length = c[platform]
                
                # Check if the next platform is within the maximum distance
                if next_platform_length <= max_distance:
                    # Move to the next platform
                    current_position += next_platform_length
                    
                    # Add the jump to the sequence
                    sequence.append(current_position)
                else:
                    # The next platform is not within the maximum distance, so we cannot move to it
                    return False
            else:
                # We are at the last platform, so we can move to the last cell
                current_position = n + 1
                
                # Add the jump to the sequence
                sequence.append(current_position)
        else:
            # The current position does not belong to a wooden platform, so we cannot move to it
            return False
    
    # If we reach here, it means that we have reached the last cell
    return True, sequence

def get_answer(n, m, d, c):
    # Check if we can reach the last cell
    can_reach, sequence = can_reach_n(n, m, d, c)
    
    # If we cannot reach the last cell, return NO
    if not can_reach:
        return "NO"
    
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Set the first and last cells to 1, as they belong to wooden platforms
    a[0] = a[n + 1] = 1
    
    # Iterate through the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Iterate through the cells of the current platform
        for j in range(length):
            # Set the cell to the index of the current platform
            a[i + j + 1] = i + 1
    
    # Iterate through the sequence of jumps
    for i in range(len(sequence)):
        # Get the current position
        current_position = sequence[i]
        
        # Set the cell to the index of the current platform
        a[current_position] = i + 1
    
    # Return the array a
    return "YES\n" + " ".join(str(x) for x in a[1:-1])

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(get_answer(n, m, d, c))

