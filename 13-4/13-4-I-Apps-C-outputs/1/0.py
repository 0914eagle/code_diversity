
def solve(k, n):
    # Initialize variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    strings = []
    count = 0
    
    # Iterate through all possible strings
    for i in range(len(alphabet) ** k):
        # Convert the index to a base-26 string
        string = base_to_string(i, k)
        
        # Check if the string is double free
        if is_double_free(string):
            # Check if the string is k-incremental
            if is_k_incremental(string, k):
                # Add the string to the list
                strings.append(string)
                count += 1
                
                # If we have found the nth string, return it
                if count == n:
                    return string
    
    # If we reach this point, no string was found, so return -1
    return -1

# Convert a number in base 10 to a string in base 26
def base_to_string(n, k):
    string = ""
    while n > 0:
        n, r = divmod(n, len(alphabet))
        string = alphabet[r] + string
    return string.zfill(k)

# Check if a string is double free
def is_double_free(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    counts = [0] * len(alphabet)
    for c in string:
        counts[alphabet.index(c)] += 1
    for i in range(1, k + 1):
        if counts.count(i) != 1:
            return False
    return True

