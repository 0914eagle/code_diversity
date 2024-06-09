
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    # Split the word into pairs of characters
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    
    # Check if any pair is an anagram of the other
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if sorted(pairs[i]) == sorted(pairs[j]):
                return pairs[i]
    
    return -1

