
def longest_substring(input_str):
    # Initialize a dictionary to store the counts of each substring
    substring_counts = {}
    
    # Initialize the longest repeated substring as an empty string
    longest_repeated_substring = ""
    
    # Iterate through the input string
    for i in range(len(input_str)):
        # Get the current substring
        current_substring = input_str[i]
        
        # Check if the substring is already in the dictionary
        if current_substring in substring_counts:
            # If it is, increment its count
            substring_counts[current_substring] += 1
            
            # If the count is greater than the length of the longest repeated substring, update the longest repeated substring
            if substring_counts[current_substring] > len(longest_repeated_substring):
                longest_repeated_substring = current_substring
        else:
            # If the substring is not in the dictionary, add it with a count of 1
            substring_counts[current_substring] = 1
    
    # Return the longest repeated substring
    return longest_repeated_substring

def main():
    input_str = input()
    longest_repeated_substring = longest_substring(input_str)
    print(longest_repeated_substring)

if __name__ == '__main__':
    main()

