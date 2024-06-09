
import sys

def solve(N, A):
    # Calculate the sum of the absolute differences
    sum_abs_diff = sum(abs(a) for a in A)
    
    # If the sum of the absolute differences is odd, there is no consistent order
    if sum_abs_diff % 2 == 1:
        return 0
    
    # Initialize the number of possible orders to 1
    num_orders = 1
    
    # Iterate over the absolute differences
    for a in A:
        # If the absolute difference is even, we can split the number of possible orders in half
        if a % 2 == 0:
            num_orders = (num_orders * (num_orders + 1)) // 2
        # If the absolute difference is odd, we need to multiply the number of possible orders by the number of possible orders for the next person
        else:
            num_orders = num_orders * (num_orders + 1)
    
    # Return the number of possible orders modulo 10^9+7
    return num_orders % (10**9 + 7)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

