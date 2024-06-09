
import math

def get_expected_inversions(n, p):
    # Initialize the number of inversions and the number of valid permutations
    inversions = 0
    valid_permutations = 0

    # Iterate over the given sequence
    for i in range(n):
        # If the current element is not -1, it is a valid permutation
        if p[i] != -1:
            valid_permutations += 1

            # Iterate over the remaining elements
            for j in range(i+1, n):
                # If the current element is not -1 and it is less than the current element, it is an inversion
                if p[j] != -1 and p[j] < p[i]:
                    inversions += 1

    # Calculate the expected number of inversions
    expected_inversions = inversions / valid_permutations

    # Calculate the value of P * Q^-1 % 998244353
    p = int(expected_inversions * 998244353)
    q = int(valid_permutations * 998244353)
    result = p * pow(q, -1, 998244353)

    return result

n = int(input())
p = list(map(int, input().split()))
result = get_expected_inversions(n, p)
print(result)

