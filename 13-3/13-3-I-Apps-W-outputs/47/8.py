
import math

def get_tape_length(n, papers):
    # Calculate the total area of all the papers
    total_area = 0
    for i in range(n-1):
        total_area += papers[i] * (2**((i+2)/4)) * (2**((i+2)/4))

    # Calculate the length of tape needed to join all the papers
    tape_length = total_area * math.sqrt(2)

    # Check if the tape length is greater than the length of an A1 paper
    if tape_length > (2**(1/4)) * (2**(1/4)):
        return "impossible"
    else:
        return tape_length

n = int(input())
papers = list(map(int, input().split()))
print(get_tape_length(n, papers))

