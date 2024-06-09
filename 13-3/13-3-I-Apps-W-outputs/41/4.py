
def is_sortable(s, k):
    # Initialize a list to store the frequencies of each letter in s
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    # Sort the frequencies in descending order
    freq.sort(reverse=True)
    
    # Check if the largest frequency is greater than or equal to k
    if freq[0] < k:
        return "No"
    
    # Iterate through the frequencies and check if they are all greater than or equal to k
    for i in range(1, len(freq)):
        if freq[i] < k * (i + 1):
            return "No"
    
    return "Yes"

