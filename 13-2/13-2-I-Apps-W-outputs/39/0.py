
import math

def get_expected_inversions(n, p):
    # Calculate the number of -1 in the input sequence
    num_of_neg_one = p.count(-1)
    
    # Calculate the number of possible valid permutations
    num_of_permutations = math.factorial(n) // math.factorial(n - num_of_neg_one)
    
    # Calculate the number of inversions in each valid permutation
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] != -1 and p[j] != -1 and p[i] > p[j]:
                inversions += 1
    
    # Calculate the expected number of inversions
    expected_inversions = inversions / num_of_permutations
    
    # Calculate the result modulo 998244353
    result = int(expected_inversions * (998244353 // num_of_permutations))
    
    return result

n = int(input())
p = list(map(int, input().split()))
print(get_expected_inversions(n, p))

