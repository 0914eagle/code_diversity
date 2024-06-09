
import sys

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def f1(N, A):
    # Calculate the sum of the absolute differences
    sum_abs_diff = sum(abs(A[i] - A[i-1]) for i in range(1, N))
    
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(N):
        num_orders *= (N - i)
    
    # Calculate the number of possible orders modulo 10^9+7
    return sum_abs_diff % (10**9 + 7) * num_orders % (10**9 + 7)

def f2(N, A):
    # Calculate the sum of the absolute differences
    sum_abs_diff = sum(abs(A[i] - A[i-1]) for i in range(1, N))
    
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(N):
        num_orders *= (N - i)
    
    # Calculate the number of possible orders modulo 10^9+7
    return sum_abs_diff % (10**9 + 7) * num_orders % (10**9 + 7)

if __name__ == '__main__':
    N, A = get_input()
    print(f1(N, A))
    print(f2(N, A))

