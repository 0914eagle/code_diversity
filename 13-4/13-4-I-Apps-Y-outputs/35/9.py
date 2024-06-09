
def solve(n, k):
    # Initialize a dictionary to store the frequency of each letter
    freq = {}
    for i in range(1, k+1):
        freq[chr(i+96)] = 0
    
    # Initialize a string to store the result
    result = ""
    
    # Iterate through the length of the string
    for i in range(n):
        # Find the letter with the minimum frequency
        min_freq = min(freq.values())
        min_key = [k for k, v in freq.items() if v == min_freq][0]
        
        # Update the frequency of the letter
        freq[min_key] += 1
        
        # Add the letter to the result string
        result += min_key
    
    return result

