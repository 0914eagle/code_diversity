
import sys

def get_possible_sums(N, K):
    # Calculate the possible sums
    possible_sums = [0] * (N + 1)
    possible_sums[0] = 1
    for i in range(1, N + 1):
        possible_sums[i] = possible_sums[i - 1] + possible_sums[i - K]
    
    # Return the number of possible sums
    return possible_sums[N]

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(get_possible_sums(N, K))

