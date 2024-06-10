
def longest_repeated_substring(input_string):
    # Initialize variables
    start_index = 0
    end_index = 0
    max_length = 0
    repeated_substring = ""

    # Iterate through the input string
    for i in range(len(input_string)):
        # Check if the substring starting at position i has been seen before
        if input_string[i] in input_string[:i]:
            # If it has, find the length of the longest repeated substring
            # starting at position i and ending at the first occurrence of the substring
            # in the input string
            start_index = i
            end_index = input_string.find(input_string[i], i)
            length = end_index - start_index + 1

            # If the length is greater than the current max length, update the max length and repeated substring
            if length > max_length:
                max_length = length
                repeated_substring = input_string[start_index:end_index+1]

    return repeated_substring

def main():
    input_string = input("Enter a string of lowercase letters: ")
    repeated_substring = longest_repeated_substring(input_string)
    print(repeated_substring)

if __name__ == '__main__':
    main()

