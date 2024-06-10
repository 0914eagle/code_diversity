
def restore_number(substring, shuffled_string):
    # Initialize a set to store the possible numbers
    numbers = set()
    
    # Iterate over the length of the shuffled string
    for i in range(1, len(shuffled_string) + 1):
        # Iterate over the possible starting positions of the substring in the shuffled string
        for j in range(len(shuffled_string) - i + 1):
            # Check if the substring is a prefix of the shuffled string
            if shuffled_string[j:j + i] == substring:
                # Add the possible number to the set
                numbers.add(int(shuffled_string[:j] + shuffled_string[j + i:]))
    
    # Return the smallest possible initial integer
    return min(numbers)

def main():
    # Read the input data
    substring = input()
    shuffled_string = input()
    
    # Call the restore_number function
    n = restore_number(substring, shuffled_string)
    
    # Print the result
    print(n)

if __name__ == '__main__':
    main()

