
import sys

def solve(H, W, C, A):
    # Initialize the minimum MP required to turn every digit on the wall into 1
    min_mp = float('inf')

    # Loop through each row of the wall
    for i in range(H):
        # Loop through each column of the wall
        for j in range(W):
            # If the current square contains a digit
            if A[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = C[A[i][j]][1]

                # If the cost is not infinite
                if cost < float('inf'):
                    # Update the minimum MP required to turn every digit on the wall into 1
                    min_mp = min(min_mp, cost)

    # Return the minimum MP required to turn every digit on the wall into 1
    return min_mp

if __name__ == '__main__':
    # Read the input from stdin
    H, W = map(int, input().split())
    C = []
    for i in range(10):
        C.append(list(map(int, input().split())))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    # Solve the problem
    print(solve(H, W, C, A))

