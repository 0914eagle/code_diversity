
def solve_problem(n, k):
    # Initialize a list to store the letters of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the frequencies of each letter
    freq = [0] * 26
    
    # Initialize a string to store the answer
    ans = ""
    
    # Loop through each letter of the alphabet
    for i in range(k):
        # Add the current letter to the answer string
        ans += alphabet[i]
        
        # Increment the frequency of the current letter
        freq[i] += 1
    
    # Loop through the remaining letters of the alphabet
    for i in range(k, 26):
        # Find the letter with the minimum frequency
        min_freq = min(freq)
        
        # Find the index of the letter with the minimum frequency
        min_idx = freq.index(min_freq)
        
        # Add the current letter to the answer string
        ans += alphabet[i]
        
        # Increment the frequency of the current letter
        freq[i] += 1
    
    # Return the answer string
    return ans

