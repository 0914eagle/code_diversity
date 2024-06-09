
import itertools

def solve(N, S1, S2):
    # Initialize the number of ways to paint the dominoes
    num_ways = 0

    # Iterate over all possible combinations of colors
    for colors in itertools.product("RGB", repeat=N):
        # Check if the current combination of colors is valid
        if is_valid_coloring(N, S1, S2, colors):
            # Increment the number of valid colorings
            num_ways += 1

    # Return the number of valid colorings modulo 1000000007
    return num_ways % 1000000007

def is_valid_coloring(N, S1, S2, colors):
    # Initialize the number of adjacent dominoes with the same color
    num_same_color_adjacent = 0

    # Iterate over all dominoes
    for i in range(N):
        # Check if the current domino is adjacent to the previous domino
        if i > 0 and S1[i] == S1[i-1]:
            # Increment the number of adjacent dominoes with the same color
            num_same_color_adjacent += 1

        # Check if the current domino is adjacent to the next domino
        if i < N-1 and S2[i] == S2[i+1]:
            # Increment the number of adjacent dominoes with the same color
            num_same_color_adjacent += 1

    # Return True if the current coloring is valid, False otherwise
    return num_same_color_adjacent <= 1

if __name__ == "__main__":
    N = int(input())
    S1 = input()
    S2 = input()
    print(solve(N, S1, S2))

