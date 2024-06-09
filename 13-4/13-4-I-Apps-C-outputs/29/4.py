
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for domino in itertools.product("RGB", repeat=N):
        paintings[domino] = 0

    # Initialize a dictionary to store the number of paintings for each pair of adjacent dominoes
    adjacents = {}
    for domino1, domino2 in itertools.combinations(range(N), 2):
        adjacents[(domino1, domino2)] = 0

    # Loop through all possible paintings of the dominoes
    for dominoes in itertools.product("RGB", repeat=N):
        # Check if the dominoes form a valid arrangement
        if is_valid_arrangement(N, S1, S2, dominoes):
            # Increment the number of paintings for each domino
            for domino in dominoes:
                paintings[domino] += 1
            # Increment the number of paintings for each pair of adjacent dominoes
            for domino1, domino2 in itertools.combinations(range(N), 2):
                adjacents[(domino1, domino2)] += 1

    # Return the number of paintings modulo 1000000007
    return sum(paintings.values()) % 1000000007

def is_valid_arrangement(N, S1, S2, dominoes):
    # Check if the dominoes form a valid arrangement
    for i in range(N):
        if S1[i] != dominoes[i] and S2[i] != dominoes[i]:
            return False
    # Check if the dominoes are adjacent by side
    for i in range(N-1):
        if dominoes[i] == dominoes[i+1] and dominoes[i] != "G":
            return False
    return True

if __name__ == "__main__":
    N = int(input())
    S1 = input()
    S2 = input()
    print(count_paintings(N, S1, S2))

