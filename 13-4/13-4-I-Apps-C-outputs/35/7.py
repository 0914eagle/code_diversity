
def longest_repeated_substring(input_string):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    substring_count = 0
    substring_start = 0
    substring_end = 0

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the current character is already in the current substring
        if input_string[i] in current_substring:
            # If it is, update the substring count and end index
            substring_count += 1
            substring_end = i
        else:
            # If it's not, update the current substring and reset the count and end index
            current_substring += input_string[i]
            substring_count = 1
            substring_end = i

        # Check if the current substring is longer than the longest substring
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
            substring_start = substring_end - len(current_substring) + 1

    # Return the longest substring
    return longest_substring[substring_start:substring_end+1]

def main():
    input_string = input("Enter a string of lowercase letters: ")
    longest_substring = longest_repeated_substring(input_string)
    print(f"The longest repeated substring is: {longest_substring}")

if __name__ == '__main__':
    main()

