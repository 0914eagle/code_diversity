
def get_bouquets(n, a, b):
    # Initialize a list to store the bouquets
    bouquets = []
    
    # Loop through each possible number of flowers in the bouquet
    for i in range(1, n + 1):
        # Check if the number of flowers is not equal to a or b
        if i != a and i != b:
            # Add the number of flowers to the list of bouquets
            bouquets.append(i)
    
    # Return the number of bouquets, modulo (10^9 + 7)
    return len(bouquets) % (10**9 + 7)

def main():
    # Read the input from stdin
    n, a, b = map(int, input().split())
    
    # Call the get_bouquets function and print the result
    print(get_bouquets(n, a, b))

if __name__ == '__main__':
    main()

