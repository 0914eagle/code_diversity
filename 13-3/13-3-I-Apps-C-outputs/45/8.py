
import sys

def solve(N, A, B):
    # Initialize the number of ways to choose tasks
    ways = 1

    # Loop through each difficulty level
    for i in range(N):
        # If there are tasks with difficulty exactly i
        if A[i] > 0:
            # Add the number of ways to choose a task with difficulty i
            ways = (ways * A[i]) % 1000000007
        # If there are tasks with difficulty either i or i+1
        if B[i] > 0:
            # Add the number of ways to choose a task with difficulty i or i+1
            ways = (ways * (B[i] + 1)) % 1000000007

    return ways

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(N, A, B))

