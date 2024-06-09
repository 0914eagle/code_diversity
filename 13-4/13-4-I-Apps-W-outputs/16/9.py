
def solve(N):
    # Initialize the minimum number of pebbles needed by Mirko to win
    min_pebbles = 1
    # Loop through each possible number of pebbles that Mirko can take
    for i in range(2, N + 1):
        # Calculate the number of pebbles that Slavko can take
        slavko_pebbles = i * 2
        # Check if Slavko can take all the remaining pebbles
        if slavko_pebbles > N:
            # If Slavko cannot take all the remaining pebbles, break the loop
            break
        # Update the minimum number of pebbles needed by Mirko to win
        min_pebbles = i
    # Return the minimum number of pebbles needed by Mirko to win
    return min_pebbles

