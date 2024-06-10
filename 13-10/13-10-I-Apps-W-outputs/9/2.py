
def get_smallest_number(substring):
    # Initialize a list to store all possible numbers
    numbers = []
    
    # Iterate through all possible lengths of the number
    for length in range(1, len(substring) + 1):
        # Iterate through all possible numbers of the current length
        for num in range(10**(length-1), 10**length):
            # Check if the current number ends with the given substring
            if str(num)[-length:] == substring:
                # If it does, add it to the list of possible numbers
                numbers.append(num)
    
    # Return the smallest possible number
    return min(numbers)

def main():
    # Read the input string and the substring
    substring = input().strip()
    input_string = input().strip()
    
    # Call the get_smallest_number function and print the result
    print(get_smallest_number(substring))

if __name__ == '__main__':
    main()

