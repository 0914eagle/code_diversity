
import sys

def get_input():
    n, a, b = map(int, sys.stdin.readline().strip().split())
    return n, a, b

def count_bouquets(n, a, b):
    # Initialize the number of bouquets to 0
    count = 0
    
    # Iterate from 1 to n, which is the number of flowers
    for i in range(1, n + 1):
        # If the current flower is not a or b, add it to the bouquet
        if i != a and i != b:
            count += 1
    
    # Return the number of bouquets
    return count

def main():
    # Get the input
    n, a, b = get_input()
    
    # Calculate the number of bouquets
    count = count_bouquets(n, a, b)
    
    # Print the number of bouquets
    print(count)

if __name__ == '__main__':
    main()

