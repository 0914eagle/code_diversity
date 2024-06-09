
def get_composite_summands(n):
    # Initialize a list to store the composite summands
    composite_summands = []
    
    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add i to the list of composite summands
            composite_summands.append(i)
    
    # Return the list of composite summands
    return composite_summands

def get_maximum_number_of_composite_summands(n):
    # Get the list of composite summands
    composite_summands = get_composite_summands(n)
    
    # Initialize a variable to store the maximum number of composite summands
    maximum_number_of_composite_summands = 0
    
    # Iterate over the list of composite summands
    for i in range(len(composite_summands)):
        # Get the current composite summand
        current_composite_summand = composite_summands[i]
        
        # Check if the current composite summand is a divisor of n
        if n % current_composite_summand == 0:
            # Add 1 to the maximum number of composite summands
            maximum_number_of_composite_summands += 1
    
    # Return the maximum number of composite summands
    return maximum_number_of_composite_summands

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate over the queries
    for i in range(q):
        # Read the current query
        n = int(input())
        
        # Get the maximum number of composite summands
        maximum_number_of_composite_summands = get_maximum_number_of_composite_summands(n)
        
        # Print the result
        if maximum_number_of_composite_summands == 0:
            print(-1)
        else:
            print(maximum_number_of_composite_summands)

if __name__ == '__main__':
    main()

