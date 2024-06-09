
import math

def get_tape_length(n, papers):
    # Calculate the area of an A1 paper
    area_a1 = 1
    for i in range(n, 0, -1):
        area_a1 *= 2 ** (1 - i / 4)

    # Calculate the total area of all papers
    total_area = 0
    for i in range(n, 0, -1):
        total_area += papers[i - 2] * area_a1 * 2 ** (1 - i / 4)

    # Calculate the total length of tape needed
    total_length = 0
    for i in range(n, 0, -1):
        total_length += papers[i - 2] * area_a1 * 2 ** (1 - i / 4) / 2

    # Check if the total area is greater than or equal to the area of an A1 paper
    if total_area >= area_a1:
        return total_length
    else:
        return "impossible"

n = int(input())
papers = list(map(int, input().split()))
print(get_tape_length(n, papers))

