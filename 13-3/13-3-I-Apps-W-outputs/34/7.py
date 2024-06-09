
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

                # If the current digit is not 1
                if A[i][j] != 1:
                    # Get the cost of turning the current digit into 4
                    cost4 = C[A[i][j]][4]

                    # If turning the current digit into 4 is cheaper than turning it into 1
                    if cost4 < cost:
                        # Update the cost to turn the current digit into 4
                        cost = cost4

                        # Get the cost of turning 4 into 9
                        cost9 = C[4][9]

                        # If turning 4 into 9 is cheaper than turning 4 into 1
                        if cost9 < cost:
                            # Update the cost to turn the current digit into 9
                            cost = cost9

                            # Get the cost of turning 9 into 1
                            cost1 = C[9][1]

                            # If turning 9 into 1 is cheaper than turning 9 into 4
                            if cost1 < cost:
                                # Update the cost to turn the current digit into 1
                                cost = cost1

                # Update the minimum MP required to turn every digit on the wall into 1
                min_mp = min(min_mp, cost)

    return min_mp

if __name__ == '__main__':
    H, W = map(int, input().split())
    C = []
    for i in range(10):
        C.append(list(map(int, input().split())))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    print(solve(H, W, C, A))

