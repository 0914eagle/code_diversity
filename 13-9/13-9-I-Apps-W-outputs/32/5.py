
import sys
import math

def get_input():
    n, a, b = map(int, sys.stdin.readline().strip().split())
    return n, a, b

def count_bouquets(n, a, b):
    # Initialize the number of bouquets to 0
    num_bouquets = 0
    
    # Iterate over all possible number of flowers in the bouquet
    for num_flowers in range(1, n + 1):
        # Check if the number of flowers is not equal to a or b
        if num_flowers != a and num_flowers != b:
            # Increment the number of bouquets
            num_bouquets += 1
    
    # Return the number of bouquets modulo (10^9 + 7)
    return num_bouquets % (10**9 + 7)

def main():
    # Read the input
    n, a, b = get_input()
    
    # Calculate the number of bouquets
    num_bouquets = count_bouquets(n, a, b)
    
    # Print the number of bouquets
    print(num_bouquets)

if __name__ == '__main__':
    main()

