
import math

def get_tape_length(n, papers):
    # Calculate the area of an A1 paper
    a1_area = 1
    for i in range(n, 0, -1):
        a1_area *= 2 ** (1 - i / 4)

    # Calculate the total area of all papers
    total_area = 0
    for i in range(n, 0, -1):
        total_area += papers[i - 2] * 2 ** (1 - i / 4)

    # Calculate the tape length needed
    tape_length = total_area / a1_area

    # Return the tape length or "impossible" if not enough paper
    if tape_length <= 10 ** 9:
        return tape_length
    else:
        return "impossible"

