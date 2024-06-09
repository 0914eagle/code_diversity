
import itertools

def count_paintings(N, S1, S2):
    # Initialize a dictionary to store the number of paintings for each domino
    paintings = {}
    for i in range(N):
        paintings[S1[i]] = 0
        paintings[S2[i]] = 0

    # Iterate over all possible combinations of paintings for the first domino
    for painting in itertools.product(range(3), repeat=N):
        # Check if the paintings are valid
        if is_valid_painting(N, S1, S2, painting):
            # Increment the number of paintings for the first domino
            paintings[S1[0]] += 1

    # Return the number of paintings for the first domino
    return paintings[S1[0]] % 1000000007

def is_valid_painting(N, S1, S2, painting):
    # Check if the paintings are valid
    for i in range(N):
        if painting[i] == painting[(i+1) % N] and S1[i] == S1[(i+1) % N]:
            return False
        if painting[i] == painting[(i+1) % N] and S2[i] == S2[(i+1) % N]:
            return False
    return True

if __name__ == '__main__':
    N = int(input())
    S1 = input()
    S2 = input()
    print(count_painting(N, S1, S2))

