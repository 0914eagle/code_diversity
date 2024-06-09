
def get_least_number_of_ones(n):
    # Initialize a list to store the addends
    addends = []
    
    # Loop until the number is 0
    while n > 0:
        # Find the largest power of 10 that is less than or equal to the number
        power = 1
        while power * 10 <= n:
            power *= 10
        
        # Add the power of 10 to the list of addends
        addends.append(power)
        
        # Subtract the power of 10 from the number
        n -= power
    
    # Return the sum of the addends
    return sum(addends)

def main():
    # Read the input from stdin
    n = int(input())
    
    # Call the function to get the least number of ones
    least_number_of_ones = get_least_number_of_ones(n)
    
    # Print the result
    print(least_number_of_ones)

if __name__ == '__main__':
    main()

