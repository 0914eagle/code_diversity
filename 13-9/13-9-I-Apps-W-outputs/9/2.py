
def get_maximum_distance(n, x, a, b):
    # Initialize the maximum distance as 0
    max_distance = 0
    
    # Loop through all possible distances between the rivals
    for distance in range(1, n):
        # Calculate the minimum number of swaps required to reach the current distance
        min_swaps = get_min_swaps(n, a, b, distance)
        
        # If the minimum number of swaps is less than or equal to the given number of swaps, update the maximum distance
        if min_swaps <= x:
            max_distance = max(max_distance, distance)
    
    # Return the maximum distance
    return max_distance

def get_min_swaps(n, a, b, distance):
    # Initialize the minimum number of swaps as 0
    min_swaps = 0
    
    # Loop through all possible positions of the rival in position a
    for pos_a in range(1, n + 1):
        # Calculate the position of the rival in position b
        pos_b = (pos_a + distance) % n + 1
        
        # If the position of the rival in position b is equal to the given position of the rival in position b, increment the minimum number of swaps
        if pos_b == b:
            min_swaps += 1
    
    # Return the minimum number of swaps
    return min_swaps

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_maximum_distance(n, x, a, b))

