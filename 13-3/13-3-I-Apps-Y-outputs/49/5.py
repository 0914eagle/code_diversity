
import sys

def solve(n, a):
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= (n - i)
    
    # Calculate the number of incorrect reports
    num_incorrect = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j] and a[i] != n-1-a[j]:
                num_incorrect += 1
    
    # Calculate the number of possible orders accounting for incorrect reports
    num_orders -= num_incorrect
    
    # Return the result modulo 10^9+7
    return num_orders % 1000000007

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

