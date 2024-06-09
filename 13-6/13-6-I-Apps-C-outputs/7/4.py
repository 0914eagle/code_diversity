
import sys

def solve(n, a):
    # Initialize the answer and the piles
    answer = 0
    piles = []

    # Iterate through each box
    for i in range(n):
        # Check if the box is available
        if a[i] > 0:
            # Find the piles that the box can be added to
            available_piles = []
            for j in range(len(piles)):
                if a[i] % piles[j][0] == 0:
                    available_piles.append(j)

            # If there are no available piles, create a new pile
            if not available_piles:
                piles.append([a[i], i])
            # Otherwise, add the box to the available piles
            else:
                for j in available_piles:
                    piles[j][0] *= a[i]
                    piles[j].append(i)

    # Return the number of piles
    return len(piles)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

