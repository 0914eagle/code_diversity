
import itertools

def count_paint_ways(N, S1, S2):
    # Initialize a dictionary to store the number of ways to paint each domino
    paint_ways = {}

    # Iterate over each domino in S1 and S2
    for i in range(N):
        for j in range(N):
            # Get the current domino
            domino = S1[i] + S2[j]

            # If the domino has not been painted yet, initialize its number of ways to paint to 0
            if domino not in paint_ways:
                paint_ways[domino] = 0

            # Increment the number of ways to paint the domino by 1
            paint_ways[domino] += 1

    # Initialize a set to store the unique ways to paint the dominoes
    unique_ways = set()

    # Iterate over each domino in S1 and S2
    for i in range(N):
        for j in range(N):
            # Get the current domino
            domino = S1[i] + S2[j]

            # If the domino has not been painted yet, add its number of ways to paint to the unique ways set
            if domino not in unique_ways:
                unique_ways.add(paint_ways[domino])

    # Return the number of unique ways to paint the dominoes, modulo 1000000007
    return sum(unique_ways) % 1000000007

