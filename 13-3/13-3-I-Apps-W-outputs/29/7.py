
import sys

def get_possible_sums(n, k):
    # Calculate the possible sums
    possible_sums = [0] * (n + 1)
    possible_sums[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            possible_sums[i] += possible_sums[j]
    possible_sums = possible_sums[k - 1:]

    # Calculate the number of possible values of the sum, modulo (10^9+7)
    num_possible_values = 0
    for i in range(len(possible_sums)):
        num_possible_values += possible_sums[i]
        num_possible_values %= 1000000007

    return num_possible_values

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_possible_sums(n, k))

