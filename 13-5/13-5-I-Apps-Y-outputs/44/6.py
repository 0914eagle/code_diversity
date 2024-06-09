
def is_possible(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Set the cell to the index of the platform
            a[j + 1] = i + 1
    
    # Initialize the current position to 0
    current_position = 0
    
    # Loop through each cell in the river
    for i in range(n + 2):
        # If the current position is not 0 or n + 1, and the cell belongs to a platform
        if current_position != 0 and current_position != n + 1 and a[current_position] != 0:
            # Jump to the next cell that belongs to the same platform
            current_position += 1
        # If the current position is not 0 or n + 1, and the cell does not belong to a platform
        elif current_position != 0 and current_position != n + 1 and a[current_position] == 0:
            # Jump to the next cell that belongs to a platform
            while current_position + d <= n + 1 and a[current_position + d] == 0:
                current_position += 1
        # If the current position is 0 or n + 1
        else:
            # Break the loop
            break
    
    # If the current position is n + 1, return YES
    if current_position == n + 1:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

def get_array(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Set the cell to the index of the platform
            a[j + 1] = i + 1
    
    # Return the array a
    return a

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(is_possible(n, m, d, c))
    print(*get_array(n, m, d, c))

