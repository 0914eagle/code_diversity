
def solve(n, k):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}
    for i in range(1, k+1):
        freq[i] = 0
    
    # Initialize a list to store the letters of the string
    s = []
    
    # Iterate through the length of the string
    for i in range(n):
        # Find the letter with the minimum frequency
        min_freq = min(freq.values())
        # Find the key (letter) with the minimum frequency
        min_key = [k for k, v in freq.items() if v == min_freq][0]
        # Increment the frequency of the letter
        freq[min_key] += 1
        # Add the letter to the string
        s.append(chr(min_key + 96))
    
    return "".join(s)

