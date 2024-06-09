
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    longest_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the longest substring
        if input_string[i] in longest_substring:
            # If it is, update the end index of the longest substring
            end_index = i
        else:
            # If it's not, check if the current substring is longer than the previous longest substring
            if len(longest_substring) < i - start_index + 1:
                longest_substring = input_string[start_index:i+1]

            # Update the start index of the longest substring
            start_index = i - len(longest_substring) + 1

    return longest_substring

def main():
    input_string = input("Enter a string of lowercase letters: ")
    longest_substring = longest_repeated_substring(input_string)
    print(f"The longest repeated substring is: {longest_substring}")

if __name__ == '__main__':
    main()

