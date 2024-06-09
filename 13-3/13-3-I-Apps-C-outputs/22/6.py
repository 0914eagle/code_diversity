
def can_obtain_array(n, q, a):
    # Initialize a dictionary to store the segments and their values
    segments = {}
    
    # Iterate over the queries
    for i in range(q):
        # Get the segment and value for the current query
        l, r, val = map(int, input().split())
        
        # Update the dictionary with the segment and value
        segments[(l, r)] = val
    
    # Initialize a set to store the covered positions
    covered = set()
    
    # Iterate over the segments
    for (l, r), val in segments.items():
        # Add the covered positions to the set
        covered |= set(range(l, r + 1))
    
    # Check if all positions are covered
    if len(covered) == n:
        return True
    else:
        return False

def restore_array(n, q, a):
    # Initialize a dictionary to store the segments and their values
    segments = {}
    
    # Iterate over the queries
    for i in range(q):
        # Get the segment and value for the current query
        l, r, val = map(int, input().split())
        
        # Update the dictionary with the segment and value
        segments[(l, r)] = val
    
    # Initialize a list to store the resulting array
    arr = [0] * n
    
    # Iterate over the segments
    for (l, r), val in segments.items():
        # Update the array with the segment and value
        for i in range(l, r + 1):
            arr[i] = val
    
    # Return the resulting array
    return arr

if __name__ == '__main__':
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    if can_obtain_array(n, q, a):
        print("YES")
        print(*restore_array(n, q, a))
    else:
        print("NO")

