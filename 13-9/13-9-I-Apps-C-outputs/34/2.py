
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    max_length = 0
    repeated_substring = ""

    # Iterate over the input string
    for i in range(len(input_string)):
        # Check if the substring starting at index i is repeated
        if input_string[i] in input_string[start_index:i]:
            # If it is repeated, find the length of the repeated substring
            repeated_substring = input_string[start_index:i]
            max_length = max(max_length, len(repeated_substring))
        # If the substring is not repeated, update the start index
        else:
            start_index = i + 1
    
    # Return the longest repeated substring
    return repeated_substring

def main():
    input_string = input()
    repeated_substring = longest_repeated_substring(input_string)
    print(repeated_substring)

if __name__ == '__main__':
    main()

