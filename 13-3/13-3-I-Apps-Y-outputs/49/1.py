
import sys

def solve(n, arr):
    # Calculate the sum of the differences
    sum_diff = sum(arr)
    
    # If the sum of the differences is odd, there is no consistent order
    if sum_diff % 2 == 1:
        return 0
    
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= (i + 1)
    
    # Return the number of possible orders modulo 10^9+7
    return num_orders % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

