
import sys

def solve(H, W, costs, A):
    # Initialize the minimum total MP required to turn every digit on the wall into 1
    min_mp = float('inf')

    # Loop through each row of the wall
    for i in range(H):
        # Loop through each column of the wall
        for j in range(W):
            # If the current square contains a digit
            if A[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = costs[A[i][j]]

                # If the cost is not zero
                if cost != 0:
                    # Get the minimum total MP required to turn the current digit into 1
                    min_mp = min(min_mp, cost)

    # Return the minimum total MP required to turn every digit on the wall into 1
    return min_mp

if __name__ == '__main__':
    H, W = map(int, input().split())
    costs = list(map(int, input().split()))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    print(solve(H, W, costs, A))

