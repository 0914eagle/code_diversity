
import math

def get_expected_inversions(n, p):
    # Calculate the number of -1 in the input sequence
    num_of_neg_one = p.count(-1)
    
    # Calculate the number of valid permutations with -1
    num_of_valid_permutations = math.factorial(n) // math.factorial(num_of_neg_one) // math.factorial(n - num_of_neg_one)
    
    # Calculate the number of inversions in each valid permutation
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] != -1 and p[j] != -1 and p[i] > p[j]:
                inversions += 1
    
    # Calculate the expected number of inversions
    expected_inversions = inversions * num_of_valid_permutations
    
    # Calculate the gcd of the expected number of inversions and the modulus
    gcd = math.gcd(expected_inversions, 998244353)
    
    # Return the result modulo the modulus
    return expected_inversions // gcd * 998244353 // gcd

n = int(input())
p = list(map(int, input().split()))
print(get_expected_inversions(n, p))

