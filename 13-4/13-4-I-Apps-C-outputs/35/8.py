
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the substring starting at position i is a repeated substring
        if input_string[i] in input_string[start_index:i]:
            # If it is, update the end index and longest substring
            end_index = i
            longest_substring = input_string[start_index:end_index+1]
        # If it's not, update the start index
        else:
            start_index = i + 1
    
    # Return the longest repeated substring
    return longest_substring

def main():
    input_string = input()
    longest_substring = longest_repeated_substring(input_string)
    print(longest_substring)

if __name__ == '__main__':
    main()

