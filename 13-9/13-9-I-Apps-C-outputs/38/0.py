
import sys

def solve(n, d):
    # Calculate the number of ways to connect the parts
    num_ways = 1
    for i in range(n):
        num_ways *= d[i]
    
    # Calculate the number of ways to connect the parts in a specific order
    num_ways_ordered = 1
    for i in range(n-1):
        num_ways_ordered *= (d[i] - 1)
    
    # Calculate the number of ways to connect the parts in a specific order with the last part
    num_ways_last = 1
    for i in range(n-1):
        num_ways_last *= (d[i+1] - 1)
    
    # Calculate the final answer by dividing the number of ways to connect the parts by the number of ways to connect the parts in a specific order
    answer = num_ways // (num_ways_ordered * num_ways_last)
    
    return answer % 998244353

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    print(solve(n, d))

