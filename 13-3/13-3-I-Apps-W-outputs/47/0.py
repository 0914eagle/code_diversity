
import math

def get_tape_length(n, papers):
    # Calculate the total area of all papers
    total_area = 0
    for i in range(n-1, 0, -1):
        total_area += papers[i-1] * (2**((i-1)/4)) * (2**((i-1)/4))

    # Calculate the length of tape needed to join all papers
    tape_length = 0
    for i in range(n-1, 0, -1):
        tape_length += papers[i-1] * (2**((i-1)/4))

    # Check if the total area is greater than the area of an A1 paper
    if total_area > (2**(1/4)) * (2**(1/4)):
        return "impossible"
    else:
        return tape_length

n = int(input())
papers = list(map(int, input().split()))
result = get_tape_length(n, papers)
print(result)

