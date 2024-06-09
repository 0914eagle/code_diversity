
def f1(n):
    # calculate the number of permutations of length n
    permutations = 1
    for i in range(n):
        permutations *= n - i
    
    # calculate the number of cyclic permutations of length n
    cyclic_permutations = 0
    for i in range(n):
        # find the largest j such that j < i and p_j > p_i
        j = n - 1
        while j >= i and permutations[j] <= permutations[i]:
            j -= 1
        
        # find the smallest j such that i < j <= n and p_j > p_i
        k = n
        while k > i and permutations[k] <= permutations[i]:
            k -= 1
        
        # if j and k exist, add the number of cyclic permutations for this prefix
        if j >= 0 and k <= n:
            cyclic_permutations += (j + 1) * (k - j)
    
    return cyclic_permutations % 1000000007

def f2(n):
    # calculate the number of permutations of length n
    permutations = 1
    for i in range(n):
        permutations *= n - i
    
    # calculate the number of cyclic permutations of length n
    cyclic_permutations = 0
    for i in range(n):
        # find the largest j such that j < i and p_j > p_i
        j = n - 1
        while j >= i and permutations[j] <= permutations[i]:
            j -= 1
        
        # find the smallest j such that i < j <= n and p_j > p_i
        k = n
        while k > i and permutations[k] <= permutations[i]:
            k -= 1
        
        # if j and k exist, add the number of cyclic permutations for this prefix
        if j >= 0 and k <= n:
            cyclic_permutations += (j + 1) * (k - j)
    
    return cyclic_permutations % 1000000007

if __name__ == '__main__':
    n = int(input())
    print(f1(n))
    print(f2(n))

