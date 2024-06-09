
def longest_non_palindrome(s):
    # Initialize variables
    longest_substring = ""
    current_substring = ""
    
    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is the same as the previous character
        if s[i] == s[i-1]:
            # If it is, append it to the current substring
            current_substring += s[i]
        else:
            # If it's not, check if the current substring is longer than the longest substring found so far
            if len(current_substring) > len(longest_substring):
                # If it is, update the longest substring
                longest_substring = current_substring
            # Reset the current substring
            current_substring = s[i]
    
    # Check if the last character is the same as the first character
    if s[0] == s[-1] and len(current_substring) > len(longest_substring):
        # If it is, update the longest substring
        longest_substring = current_substring
    
    # Return the length of the longest substring
    return len(longest_substring)

