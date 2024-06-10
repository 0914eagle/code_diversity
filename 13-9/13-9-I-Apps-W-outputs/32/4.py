
import sys

def get_input():
    n, a, b = map(int, sys.stdin.readline().strip().split())
    return n, a, b

def get_bouquets(n, a, b):
    # Initialize a list to store the bouquets
    bouquets = []
    
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # If the current number is not equal to a and not equal to b, add it to the bouquet
        if i != a and i != b:
            bouquets.append(i)
    
    # Return the number of bouquets
    return len(bouquets)

def main():
    # Get the input
    n, a, b = get_input()
    
    # Calculate the number of bouquets
    bouquets = get_bouquets(n, a, b)
    
    # Print the result
    print(bouquets)

if __name__ == '__main__':
    main()

