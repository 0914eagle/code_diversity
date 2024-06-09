
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the substring starting from the current index is already present in the input string
        if input_string[i:].startswith(input_string[:i]):
            # If it is, update the start and end indices and the longest substring
            start_index = i
            end_index = start_index + len(input_string[:i]) - 1
            longest_substring = input_string[start_index:end_index+1]

    # Return the longest substring
    return longest_substring

def main():
    input_string = input()
    longest_substring = longest_repeated_substring(input_string)
    print(longest_substring)

if __name__ == '__main__':
    main()

