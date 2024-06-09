
import sys

def solve(N, A):
    # Calculate the sum of the absolute differences
    sum_abs_diff = sum(abs(x) for x in A)
    
    # If the sum of the absolute differences is odd, then there is no consistent order
    if sum_abs_diff % 2 == 1:
        return 0
    
    # Initialize the number of possible orders to 1
    num_orders = 1
    
    # Iterate over the absolute differences
    for i in range(N):
        # If the absolute difference is even, then we can have both left and right orders
        if A[i] % 2 == 0:
            num_orders *= 2
        # If the absolute difference is odd, then we can only have one order
        else:
            num_orders *= 1
    
    # Return the number of possible orders modulo 10^9+7
    return num_orders % (10**9+7)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

