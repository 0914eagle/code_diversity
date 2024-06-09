
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Initialize a set to store the colors of the dominoes in the first row
    first_row = set()
    for i in range(N):
        first_row.add(S1[i])
        first_row.add(S2[i])

    # Iterate over the dominoes in the first row and calculate the number of paintings for each domino
    for domino in first_row:
        paintings[domino] += 1

    # Iterate over the remaining dominoes and calculate the number of paintings for each domino
    for i in range(1, N):
        for domino in itertools.product("RGB", repeat=N-i):
            paintings[domino] += sum(1 for color in domino if color != first_row[i-1])

    # Return the total number of paintings modulo 1000000007
    return sum(paintings.values()) % 1000000007

