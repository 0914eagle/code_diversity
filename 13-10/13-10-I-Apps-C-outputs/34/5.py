
import sys

def get_palindromic_strings(s):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []
    
    # Iterate over the length of the input string
    for length in range(len(s), 2*len(s)):
        # Iterate over the starting index of the substring
        for start_index in range(len(s) - length + 1):
            # Extract the substring from the input string
            substring = s[start_index:start_index + length]
            
            # Check if the substring is palindromic
            if substring == substring[::-1]:
                # Add the substring to the list of palindromic strings
                palindromic_strings.append(substring)
    
    # Return the list of palindromic strings
    return palindromic_strings

def count_palindromic_strings(s):
    # Get the list of palindromic strings
    palindromic_strings = get_palindromic_strings(s)
    
    # Initialize a counter variable
    count = 0
    
    # Iterate over the list of palindromic strings
    for string in palindromic_strings:
        # Increment the counter variable
        count += 1
    
    # Return the count modulo 10^9 + 7
    return count % (10**9 + 7)

def main():
    # Read the input string
    s = input()
    
    # Call the count_palindromic_strings function
    count = count_palindromic_strings(s)
    
    # Print the count
    print(count)

if __name__ == '__main__':
    main()

