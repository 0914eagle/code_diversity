
import math

def get_tape_length(n, papers):
    # Calculate the area of an A1 paper
    a1_area = 1
    for i in range(n, 0, -1):
        a1_area *= 2 ** (1 / 4)
    
    # Calculate the total area of all papers
    total_area = 0
    for i in range(n, 0, -1):
        total_area += papers[i - 2] * a1_area / (2 ** ((i - 1) / 4))
    
    # Calculate the total length of tape needed
    tape_length = total_area ** 0.5
    
    # Check if the total length of tape is less than or equal to 10^9 meters
    if tape_length <= 10 ** 9:
        return tape_length
    else:
        return "impossible"

n = int(input())
papers = list(map(int, input().split()))
print(get_tape_length(n, papers))

