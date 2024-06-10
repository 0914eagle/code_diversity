
def get_longest_repeated_substring(input_string):
    # Initialize a dictionary to store the length and starting index of each repeated substring
    repeated_substrings = {}
    
    # Loop through the input string
    for i in range(len(input_string)):
        # Check if the current substring has been encountered before
        if input_string[i] in repeated_substrings:
            # If it has, update the length and starting index of the repeated substring
            repeated_substrings[input_string[i]][0] += 1
            repeated_substrings[input_string[i]][1] = i - repeated_substrings[input_string[i]][0] + 1
        else:
            # If it hasn't, add it to the dictionary with a length of 1 and the current index as the starting index
            repeated_substrings[input_string[i]] = [1, i]
    
    # Find the longest repeated substring
    longest_substring = ""
    for key, value in repeated_substrings.items():
        if value[0] > len(longest_substring):
            longest_substring = input_string[value[1]:value[1] + value[0]]
    
    return longest_substring

def main():
    input_string = input()
    print(get_longest_repeated_substring(input_string))

if __name__ == '__main__':
    main()

