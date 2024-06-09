
def get_least_number_of_ones(n):
    # Initialize a list to store the addends
    addends = []
    # Initialize a variable to store the current addend
    current_addend = 1
    # Loop until the current addend is greater than the given number
    while current_addend <= n:
        # If the current addend is a multiple of 10, add it to the list of addends
        if current_addend % 10 == 0:
            addends.append(current_addend)
        # Add 1 to the current addend
        current_addend += 1
    # Return the length of the list of addends
    return len(addends)

def main():
    # Read a line of input from stdin and convert it to an integer
    n = int(input().strip())
    # Call the get_least_number_of_ones function and store the result in a variable
    result = get_least_number_of_ones(n)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

