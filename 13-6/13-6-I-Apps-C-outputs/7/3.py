
import math

def solve(n, boxes):
    # Initialize the answer and the piles
    answer = 0
    piles = []

    # Iterate through each box
    for i in range(n):
        # Check if the current box is divisible by any of the previous boxes
        for j in range(i):
            if boxes[i] % boxes[j] == 0:
                # If it is, add it to the current pile
                piles[-1].append(boxes[i])
                break
        else:
            # If it is not divisible by any of the previous boxes, start a new pile
            piles.append([boxes[i]])

    # Calculate the number of distinct piles
    answer = len(piles)

    # Return the answer modulo 10^9 + 7
    return answer % (10**9 + 7)

