
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop until the string is of the required length
    while len(result) < n:
        # Find the letter with the minimum frequency
        min_freq_idx = freq.index(min(freq))
        # Add the letter to the result string
        result += chr(ord('a') + min_freq_idx)
        # Increment the frequency of the letter
        freq[min_freq_idx] += 1
    # Return the result string
    return result

def f1(...):
    ...
    return ...

def f2(...):
    ...
    return ...

if __name__ == '__main__':
    ...

