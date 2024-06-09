
import itertools

def paint_dominoes(N, S1, S2):
    # Initialize a dictionary to store the number of ways to paint each domino
    num_ways = {}

    # Iterate over each domino in S1 and S2
    for i in range(N):
        for j in range(i+1, N):
            # Get the colors of the two dominoes
            color1 = S1[i]
            color2 = S2[j]

            # If the dominoes are not adjacent, they can be painted with any color
            if i != j-1 and i != j+1:
                num_ways[(color1, color2)] = 3
            # If the dominoes are adjacent, they must be painted with different colors
            else:
                num_ways[(color1, color2)] = 2

    # Calculate the total number of ways to paint the dominoes
    total_ways = 1
    for key, value in num_ways.items():
        total_ways *= value

    # Return the total number of ways to paint the dominoes, modulo 1000000007
    return total_ways % 1000000007

