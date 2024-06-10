
def count_occurrences(s):
    # Initialize a dictionary to store the count of each hidden string
    hidden_strings = {}
    
    # Iterate over the characters of the string
    for i in range(len(s)):
        # Check if the current character is already a key in the dictionary
        if s[i] in hidden_strings:
            # If it is, increment the count of the hidden string
            hidden_strings[s[i]] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            hidden_strings[s[i]] = 1
    
    # Return the maximum count of any hidden string
    return max(hidden_strings.values())

def main():
    s = input()
    print(count_occurrences(s))

if __name__ == '__main__':
    main()

