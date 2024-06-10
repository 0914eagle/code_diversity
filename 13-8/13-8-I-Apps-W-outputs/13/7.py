
def get_good_strings(s):
    # Initialize variables
    good_strings = []
    current_string = ""
    
    # Iterate through the input string
    for char in s:
        # If the current character is different from the previous character, add the current string to the list of good strings
        if len(current_string) > 0 and current_string[-1] != char:
            good_strings.append(current_string)
            current_string = ""
        # Add the current character to the current string
        current_string += char
    
    # Add the last string to the list of good strings
    if len(current_string) > 0:
        good_strings.append(current_string)
    
    return good_strings

def solve(s):
    # Get the list of good strings
    good_strings = get_good_strings(s)
    
    # Initialize the minimum number of good strings
    min_good_strings = len(good_strings)
    
    # Initialize the minimum concatenation of good strings
    min_concatenation = ""
    
    # Iterate through all possible combinations of good strings
    for i in range(len(good_strings)):
        for combination in itertools.combinations(good_strings, i + 1):
            # Concatenate the current combination of good strings
            concatenation = "".join(combination)
            
            # If the concatenation is equal to the input string and has fewer good strings than the current minimum, update the minimum
            if concatenation == s and len(combination) < min_good_strings:
                min_good_strings = len(combination)
                min_concatenation = concatenation
    
    # Return the minimum number of good strings and the minimum concatenation of good strings
    return min_good_strings, min_concatenation

def main():
    # Read the input string
    n = int(input())
    s = input()
    
    # Solve the problem
    min_good_strings, min_concatenation = solve(s)
    
    # Print the output
    print(min_good_strings)
    print(" ".join(min_concatenation))

if __name__ == '__main__':
    main()

