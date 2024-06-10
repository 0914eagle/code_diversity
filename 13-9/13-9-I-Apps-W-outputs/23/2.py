
def get_good_strings(s):
    # Initialize variables
    good_strings = []
    current_string = ""
    
    # Iterate through the input string
    for char in s:
        # If the current character is different from the previous character, add the current string to the list of good strings
        if current_string and current_string[-1] != char:
            good_strings.append(current_string)
            current_string = ""
        # Add the current character to the current string
        current_string += char
    
    # Add the last string to the list of good strings
    if current_string:
        good_strings.append(current_string)
    
    return good_strings

def get_minimal_cut(s):
    # Get all good substrings of the input string
    good_strings = get_good_strings(s)
    
    # Initialize variables
    minimal_cut = len(good_strings)
    minimal_cut_strings = []
    
    # Iterate through all possible combinations of good substrings
    for i in range(len(good_strings)):
        for combination in itertools.combinations(good_strings, i + 1):
            # Check if the concatenation of the current combination is equal to the input string
            if "".join(combination) == s:
                # If it is, check if the current combination has a smaller number of substrings than the previous minimum
                if len(combination) < minimal_cut:
                    minimal_cut = len(combination)
                    minimal_cut_strings = list(combination)
    
    return minimal_cut, minimal_cut_strings

def main():
    # Read the input string
    n = int(input())
    s = input()
    
    # Get the minimal cut
    minimal_cut, minimal_cut_strings = get_minimal_cut(s)
    
    # Print the result
    print(minimal_cut)
    print(" ".join(minimal_cut_strings))

if __name__ == '__main__':
    main()

