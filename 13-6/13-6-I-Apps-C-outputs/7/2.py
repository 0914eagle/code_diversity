
import sys

def solve(n, a):
    # Initialize the answer and the piles
    ans = 0
    piles = []

    # Loop through each box
    for i in range(n):
        # Check if the current box is divisible by any of the previous boxes
        for j in range(i):
            if a[i] % a[j] == 0:
                # If it is, add it to the current pile
                piles[-1].append(a[i])
                break
        else:
            # If it is not divisible by any of the previous boxes, create a new pile
            piles.append([a[i]])

    # Return the number of piles
    return len(piles)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

