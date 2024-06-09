
import itertools

def get_nth_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible combinations of lowercase letters
    for letters in itertools.combinations_with_replacement("abcdefghijklmnopqrstuvwxyz", k):
        # Check if the current combination is double free and k-incremental
        if is_double_free(letters) and is_k_incremental(letters, k):
            # Add the current string to the list of generated strings
            strings.append("".join(letters))
            
            # If the list of generated strings has reached the desired length, return the nth string
            if len(strings) == n:
                return strings[n-1]
    
    # If no string was found, return -1
    return -1

# Check if a string is double free
def is_double_free(string):
    # Check if any two adjacent characters in the string are the same
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to store the frequency of each character in the string
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    # Check if the frequency of each character is k-incremental
    for char, count in freq.items():
        if count != k:
            return False
    return True

print(get_nth_string(2, 650))
print(get_nth_string(2, 651))

