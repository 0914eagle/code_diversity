
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""
    current_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the current substring
        if input_string[i] in current_substring:
            # If it is, update the start index of the current substring
            start_index = current_substring.index(input_string[i]) + 1
            # Update the current substring to include the current character
            current_substring = current_substring[start_index:] + input_string[i]
        else:
            # If it's not, add the current character to the current substring
            current_substring += input_string[i]

        # Check if the current substring is longer than the longest substring
        if len(current_substring) > len(longest_substring):
            # If it is, update the longest substring
            longest_substring = current_substring

    return longest_substring

def main():
    input_string = input("Enter a string of lowercase letters: ")
    longest_substring = longest_repeated_substring(input_string)
    print(f"The longest repeated substring is: {longest_substring}")

if __name__ == '__main__':
    main()

