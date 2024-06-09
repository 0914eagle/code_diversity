
import sys

def solve(n, a):
    # Calculate the sum of the absolute differences
    sum_abs_diff = sum(abs(a[i] - a[i-1]) for i in range(1, n))
    
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= i + 1
    
    # Calculate the number of possible orders with the given absolute differences
    num_orders_with_abs_diff = 1
    for i in range(n):
        num_orders_with_abs_diff *= (i + 1 - a[i])
    
    # Calculate the final answer
    answer = num_orders_with_abs_diff * num_orders // sum_abs_diff
    
    return answer % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

