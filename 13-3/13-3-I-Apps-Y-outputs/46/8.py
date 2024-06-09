
import sys

def get_input():
    n = int(input())
    lengths = list(map(int, input().split()))
    return n, lengths

def solve(n, lengths):
    # Sort the lengths in non-decreasing order
    lengths.sort()
    
    # Initialize the number of triples to 0
    num_triples = 0
    
    # Iterate over all possible values of i
    for i in range(n - 2):
        # Find the smallest length that is greater than the sum of the lengths of the first two sticks
        j = i + 1
        while j < n - 1 and lengths[i] + lengths[j] > lengths[j + 1]:
            j += 1
        
        # If a valid j is found, increment the number of triples
        if j < n - 1:
            num_triples += 1
    
    return num_triples

n, lengths = get_input()
print(solve(n, lengths))

