
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Initialize a dictionary to store the number of paintings for each pair of adjacent dominoes
    adjacent_paintings = {}
    for pair in itertools.product("RGB", repeat=2):
        adjacent_paintings[pair] = 0

    # Loop through each domino in S1 and S2 and increment the number of paintings for each domino
    for i in range(N):
        for j in range(i+1, N):
            # Get the colors of the two dominoes
            color1 = S1[i]
            color2 = S2[j]
            # Get the colors of the two adjacent dominoes
            adjacent_color1 = S1[i-1] if i > 0 else "G"
            adjacent_color2 = S2[j-1] if j > 0 else "G"
            # Increment the number of paintings for the two dominoes
            paintings[(color1, color2)] += 1
            # Increment the number of paintings for the two adjacent dominoes
            adjacent_paintings[(adjacent_color1, adjacent_color2)] += 1

    # Initialize the total number of paintings to 0
    total_paintings = 0
    # Loop through each domino and add the number of paintings for that domino to the total
    for domino in paintings:
        total_paintings += paintings[domino]

    # Return the total number of paintings modulo 1000000007
    return total_paintings % 1000000007

