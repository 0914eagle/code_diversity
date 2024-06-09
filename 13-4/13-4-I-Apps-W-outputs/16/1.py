
def solve(N):
    # Initialize the minimum number of pebbles to take
    min_pebbles = 1
    # Loop through each possible number of pebbles to take
    for i in range(2, N + 1):
        # Check if the current number of pebbles is a valid move for Mirko
        if i % 2 == 1:
            # If the current number of pebbles is odd, it is a valid move for Mirko
            min_pebbles = i
            break
    return min_pebbles

