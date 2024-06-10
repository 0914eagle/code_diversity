
def get_bouquets(n, a, b):
    # Initialize a list to store the bouquets
    bouquets = []
    
    # Loop through each possible number of flowers in the bouquet
    for i in range(1, n + 1):
        # If the number of flowers is not equal to a or b, add it to the bouquets list
        if i != a and i != b:
            bouquets.append(i)
    
    # Return the number of bouquets modulo (10^9 + 7)
    return len(bouquets) % (10**9 + 7)

def main():
    # Read the input data
    n, a, b = map(int, input().split())
    
    # Call the get_bouquets function and print the result
    print(get_bouquets(n, a, b))

if __name__ == '__main__':
    main()

