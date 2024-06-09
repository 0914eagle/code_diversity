
import sys

def solve(N, X, A):
    # Initialize the count of different integers not exceeding X to 0
    count = 0

    # Iterate over the given integers A_i
    for i in range(N):
        # Check if the current integer A_i is not greater than X
        if A[i] <= X:
            # Increment the count of different integers not exceeding X
            count += 1

            # Check if the current integer A_i is not equal to X
            if A[i] != X:
                # Double the current integer A_i and add it to the count
                count += 1

    # Return the count of different integers not exceeding X
    return count % 998244353

if __name__ == '__main__':
    # Read the input from stdin
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # Solve the problem
    print(solve(N, X, A))

