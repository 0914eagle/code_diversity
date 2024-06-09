
import math

def get_expected_inversions(n, p):
    # Calculate the number of -1 in the sequence
    num_of_ones = p.count(1)
    
    # Calculate the number of valid permutations
    num_of_permutations = math.factorial(n) // math.factorial(n - num_of_ones)
    
    # Calculate the number of inversions in each valid permutation
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] != -1 and p[j] != -1 and p[i] > p[j]:
                inversions += 1
    
    # Calculate the expected number of inversions
    expected_inversions = inversions / num_of_permutations
    
    # Calculate the value of P \* Q^-1 % 998244353
    p = int(expected_inversions * num_of_permutations)
    q = int(num_of_permutations)
    result = p * pow(q, -1, 998244353)
    
    return result

n = int(input())
p = list(map(int, input().split()))
print(get_expected_inversions(n, p))

