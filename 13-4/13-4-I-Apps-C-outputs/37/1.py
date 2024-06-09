
def solve(k, n):
    # Initialize variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    strings = []
    count = 0
    
    # Iterate through all possible strings
    for i in range(len(alphabet) ** k):
        # Convert the index to a string
        string = ""
        for j in range(k):
            string += alphabet[(i // (len(alphabet) ** j)) % len(alphabet)]
        
        # Check if the string is double free and k-incremental
        if is_double_free(string) and is_k_incremental(string, k):
            count += 1
            strings.append(string)
        
        # If the count reaches the desired index, return the string
        if count == n:
            return strings[-1]
    
    # If no string is found, return -1
    return -1

# Check if a string is double free
def is_double_free(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to keep track of the frequency of each character
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    # Check if the frequency of each character is k-incremental
    for char, freq in freq.items():
        if freq != k:
            return False
    return True

print(solve(2, 650))
print(solve(2, 651))

