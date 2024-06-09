
def f1(a, b):
    # Calculate the sum of the products of elements in a and b
    sum_prod = 0
    for i in range(len(a)):
        sum_prod += a[i] * b[i]
    
    # Return the sum of the products modulo 998244353
    return sum_prod % 998244353

def f2(b):
    # Sort the elements of b in non-decreasing order
    b.sort()
    
    # Calculate the sum of the products of elements in a and b
    sum_prod = 0
    for i in range(len(b)):
        sum_prod += b[i]
    
    # Return the sum of the products modulo 998244353
    return sum_prod % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(a, b))
    print(f2(b))

