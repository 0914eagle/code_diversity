
import itertools

def get_nth_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible combinations of lowercase letters
    for letters in itertools.combinations_with_replacement("abcdefghijklmnopqrstuvwxyz", k):
        # Check if the current combination is double free and $k$-incremental
        if is_double_free(letters) and is_k_incremental(letters, k):
            # Add the current string to the list of generated strings
            strings.append("".join(letters))
            
            # If the list of generated strings has reached the desired length, return the $n^\mathrm {th}$ string
            if len(strings) == n:
                return strings[n-1]
    
    # If no string was found, return -1
    return -1

# Check if a string is double free
def is_double_free(string):
    # Check if any two adjacent letters are the same
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

# Check if a string is $k$-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}
    for letter in string:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1
    
    # Check if the frequency of each letter is $j$ for some $j$ in the range [1, k]
    for letter, count in freq.items():
        if count not in range(1, k+1):
            return False
    return True

n = int(input())
k = int(input())
print(get_nth_string(k, n))

