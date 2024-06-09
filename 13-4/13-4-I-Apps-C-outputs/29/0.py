
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Iterate over the dominoes in S1 and S2 and increment the number of paintings for each domino
    for i in range(N):
        for j in range(i+1, N):
            if S1[i] != S1[j] and S2[i] != S2[j]:
                paintings[(S1[i], S2[i])] += 1
                paintings[(S1[j], S2[j])] += 1
            elif S1[i] != S1[j] or S2[i] != S2[j]:
                paintings[(S1[i], S2[i])] += 1
                paintings[(S1[j], S2[j])] += 1

    # Return the sum of the number of paintings for each domino, modulo 1000000007
    return sum(paintings.values()) % 1000000007

