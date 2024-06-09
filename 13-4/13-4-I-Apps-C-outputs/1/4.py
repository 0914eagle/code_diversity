
def get_k_incremental_double_free_string(k, n):
    
    import itertools
    
    # Generate all possible k-incremental strings
    k_incremental_strings = []
    for letters in itertools.product(range(97, 123), repeat=k):
        letter_counts = [0] * 26
        for letter in letters:
            letter_counts[letter - 97] += 1
        if all(letter_counts[i] == i for i in range(k)):
            k_incremental_strings.append(''.join(chr(97 + letter) for letter in letters))
    
    # Filter out non-double-free strings
    double_free_strings = []
    for string in k_incremental_strings:
        if all(string[i] != string[i + 1] for i in range(len(string) - 1)):
            double_free_strings.append(string)
    
    # Return the nth string in alphabetical order
    return double_free_strings[n - 1] if n <= len(double_free_strings) else -1

