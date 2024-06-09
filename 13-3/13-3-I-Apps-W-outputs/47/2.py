
import math

def get_tape_length(n, papers):
    # Calculate the area of an A1 paper
    a1_area = 1
    for i in range(n, 1, -1):
        a1_area *= 2
    
    # Calculate the total area of all papers
    total_area = 0
    for i in range(n, 0, -1):
        total_area += papers[i-1] * (2**((i-1)/4) * 2**((i-1)/2))
    
    # Check if Björn has enough paper to make an A1 paper
    if total_area < a1_area:
        return "impossible"
    
    # Calculate the total length of tape needed
    total_length = 0
    for i in range(n, 0, -1):
        total_length += papers[i-1] * (2**((i-1)/4))
    
    return total_length

n = int(input())
papers = list(map(int, input().split()))
result = get_tape_length(n, papers)
print(result)

