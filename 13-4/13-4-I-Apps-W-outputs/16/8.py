
def solve(N):
    # Initialize the minimum number of pebbles that Mirko must take during his first turn
    min_pebbles = 1
    # Initialize the maximum number of pebbles that Slavko can take during his turn
    max_pebbles = 1
    # Iterate through the remaining pebbles in the heap
    for i in range(2, N+1):
        # If Mirko takes i pebbles, Slavko can take at most 2i-1 pebbles
        if i <= max_pebbles:
            # Update the minimum number of pebbles that Mirko must take during his first turn
            min_pebbles = i
            # Update the maximum number of pebbles that Slavko can take during his turn
            max_pebbles = 2*i-1
    return min_pebbles

