
def f1(n, a, b):
    # Calculate the sum of the products of elements in a and b
    sum_products = 0
    for i in range(n):
        sum_products += a[i] * b[i]
    
    # Return the sum of the products modulo 998244353
    return sum_products % 998244353

def f2(n, a, b):
    # Initialize the minimum sum to a large value
    min_sum = 1000000000
    
    # Iterate over all possible permutations of b
    for perm in itertools.permutations(b):
        # Calculate the sum of the products of elements in a and b for this permutation
        sum_products = 0
        for i in range(n):
            sum_products += a[i] * perm[i]
        
        # Update the minimum sum if this permutation has a smaller sum
        if sum_products < min_sum:
            min_sum = sum_products
    
    # Return the minimum sum modulo 998244353
    return min_sum % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f2(n, a, b))

