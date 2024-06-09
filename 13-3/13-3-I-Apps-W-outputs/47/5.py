
import math

def get_tape_length(n, papers):
    # Calculate the total area of all papers
    total_area = 0
    for i in range(n-1, 0, -1):
        total_area += papers[i-1] * (2**((i-1)/4)) * (2**((i-1)/4))

    # Calculate the length of tape needed to join two papers together
    tape_length = 2 * (2**((n-1)/4))

    # Calculate the total length of tape needed
    total_tape_length = tape_length * math.ceil(total_area / (2**((n-1)/4)))

    return total_tape_length

n = int(input())
papers = list(map(int, input().split()))

if n < 2 or n > 30:
    print("impossible")
else:
    total_tape_length = get_tape_length(n, papers)
    print(f"{total_tape_length:.5f}")

