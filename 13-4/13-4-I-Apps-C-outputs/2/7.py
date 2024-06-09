
import sys

def get_number_of_ways(r, w, d):
    # Initialize the number of ways to be 0
    number_of_ways = 0

    # Iterate over all possible combinations of red and white wine piles
    for i in range(1, r + 1):
        for j in range(1, w + 1):
            # Check if the current combination satisfies the conditions
            if i + j <= r and i <= d:
                # Increment the number of ways
                number_of_ways += 1

    # Return the number of ways modulo 10^9 + 7
    return number_of_ways % (10**9 + 7)

if __name__ == '__main__':
    r, w, d = map(int, sys.stdin.readline().split())
    print(get_number_of_ways(r, w, d))

