
import sys

def count_distinct_strings(S):
    # Initialize a set to store the distinct strings
    distinct_strings = set()
    
    # Loop through each character in the string
    for i in range(len(S)):
        # If the current character is not equal to the next character
        if S[i] != S[i+1]:
            # Replace the current character with the character that is different from both the current and next characters
            S = S[:i] + "C" + S[i+2:]
            # Add the modified string to the set of distinct strings
            distinct_strings.add(S)
    
    # Return the number of distinct strings
    return len(distinct_strings)

if __name__ == '__main__':
    # Read the input string from stdin
    S = sys.stdin.readline().strip()
    
    # Call the count_distinct_strings function and print the result
    print(count_distinct_strings(S))

