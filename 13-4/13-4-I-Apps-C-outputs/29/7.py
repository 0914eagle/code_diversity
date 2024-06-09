
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Iterate over the dominoes in S1 and S2 and increment the number of paintings for each domino
    for i in range(N):
        for j in range(N):
            domino1 = S1[i]
            domino2 = S2[j]
            if domino1 != domino2:
                paintings[(domino1, domino2)] += 1

    # Return the sum of the number of paintings for all dominoes, modulo 1000000007
    return sum(paintings.values()) % 1000000007

