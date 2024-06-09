
import math

def f1(a, b):
    # Calculate the sum of the products of elements in a and b
    sum_prod = 0
    for i in range(len(a)):
        sum_prod += a[i] * b[i]
    
    # Return the sum modulo 998244353
    return sum_prod % 998244353

def f2(a, b):
    # Calculate the sum of the products of elements in a and b, but with the elements of b rearranged
    sum_prod = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum_prod += a[i] * b[j]
    
    # Return the sum modulo 998244353
    return sum_prod % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Calculate the sum of the products of elements in a and b
    sum_prod_1 = f1(a, b)
    
    # Calculate the sum of the products of elements in a and b, but with the elements of b rearranged
    sum_prod_2 = f2(a, b)
    
    # Print the minimum of the two sums modulo 998244353
    print(min(sum_prod_1, sum_prod_2) % 998244353)

