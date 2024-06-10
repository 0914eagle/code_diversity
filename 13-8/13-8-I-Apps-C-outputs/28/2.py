
def hidden_string(s):
    # Initialize a dictionary to store the hidden strings and their indices
    hidden_strings = {}
    
    # Loop through the string and check if the current character is part of a hidden string
    for i in range(len(s)):
        # If the current character is not the first character of a hidden string, skip it
        if i > 0 and s[i] == s[i-1]:
            continue
        
        # Initialize a list to store the indices of the hidden string
        indices = [i]
        
        # Loop through the remaining characters of the string and check if they are part of the hidden string
        for j in range(i+1, len(s)):
            # If the current character is not part of the hidden string, break the loop
            if s[j] != s[i]:
                break
            # Otherwise, add the index of the current character to the list of indices
            indices.append(j)
        
        # If the hidden string has at least two characters, add it to the dictionary with its indices
        if len(indices) >= 2:
            hidden_strings[s[i]] = indices
    
    # Initialize a variable to store the number of occurrences of the secret message
    num_occurrences = 0
    
    # Loop through the dictionary of hidden strings and their indices
    for hidden_string, indices in hidden_strings.items():
        # If the hidden string has more than one index, it is a secret message
        if len(indices) > 1:
            # Increment the number of occurrences of the secret message
            num_occurrences += 1
    
    # Return the number of occurrences of the secret message
    return num_occurrences

def main():
    # Read a string from stdin
    s = input()
    
    # Print the number of occurrences of the secret message
    print(hidden_string(s))

if __name__ == '__main__':
    main()

