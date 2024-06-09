
def is_possible_to_reach(n, m, d, c):
    # Initialize the array a
    a = [0] * (n + 2)
    
    # Set the leftmost and rightmost cells as belonging to platform 1
    a[0] = 1
    a[n + 1] = 1
    
    # Iterate through the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Iterate through the cells of the current platform
        for j in range(length):
            # Set the current cell as belonging to the current platform
            a[j + 1] = i + 1
    
    # Initialize the maximum distance of jump
    max_distance = d
    
    # Initialize the current position as 0
    current_position = 0
    
    # Initialize the sequence of jumps
    jumps = []
    
    # Iterate until the current position is n + 1
    while current_position < n + 1:
        # Check if the current position is a platform
        if a[current_position] != 0:
            # Get the index of the platform
            platform_index = a[current_position]
            
            # Check if the platform index is within the range of platforms
            if platform_index <= m:
                # Get the length of the platform
                platform_length = c[platform_index - 1]
                
                # Check if the platform length is greater than the maximum distance of jump
                if platform_length > max_distance:
                    # Return False
                    return False
                else:
                    # Add the current position to the sequence of jumps
                    jumps.append(current_position)
                    
                    # Update the current position
                    current_position += platform_length
            else:
                # Return False
                return False
        else:
            # Return False
            return False
    
    # Check if the sequence of jumps is valid
    if len(jumps) == n + 1:
        # Return True
        return True
    else:
        # Return False
        return False

def get_array(n, m, d, c):
    # Initialize the array a
    a = [0] * (n + 2)
    
    # Set the leftmost and rightmost cells as belonging to platform 1
    a[0] = 1
    a[n + 1] = 1
    
    # Iterate through the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Iterate through the cells of the current platform
        for j in range(length):
            # Set the current cell as belonging to the current platform
            a[j + 1] = i + 1
    
    # Return the array a
    return a

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    if is_possible_to_reach(n, m, d, c):
        a = get_array(n, m, d, c)
        print("YES")
        print(" ".join(map(str, a[1:-1])))
    else:
        print("NO")

