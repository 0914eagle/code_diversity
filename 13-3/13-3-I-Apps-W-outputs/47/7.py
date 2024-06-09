
import math

def get_tape_length(n, papers):
    # Calculate the area of an A1 paper
    area_a1 = 1
    for i in range(n, 1, -1):
        area_a1 *= 2
    
    # Calculate the total area of all papers
    total_area = 0
    for i in range(n, 0, -1):
        total_area += papers[i-1] * area_a1 / (2**((i-1)/2))
    
    # Calculate the total length of tape needed
    tape_length = 0
    for i in range(n, 0, -1):
        tape_length += papers[i-1] * area_a1 / (2**((i-1)/2))
    
    return tape_length

def main():
    n = int(input())
    papers = list(map(int, input().split()))
    tape_length = get_tape_length(n, papers)
    print(tape_length)

if __name__ == "__main__":
    main()

