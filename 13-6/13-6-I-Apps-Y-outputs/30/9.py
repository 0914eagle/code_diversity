
def is_multigram(word):
    if len(word) < 3:
        return -1
    
    # Split the word into pairs of consecutive letters
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    
    # Check if all pairs are anagrams
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if pairs[i] != pairs[j]:
                return -1
    
    # If all pairs are anagrams, find the shortest root
    roots = set()
    for i in range(1, len(word)):
        if word[:i] == word[i:]:
            roots.add(word[:i])
    
    return min(roots)

