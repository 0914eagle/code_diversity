
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    # split the word into pairs of characters
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    
    # check if each pair is an anagram
    for pair in pairs:
        if not is_anagram(pair):
            return -1
    
    # find the shortest root
    roots = set()
    for i in range(1, len(word)):
        if is_anagram(word[:i]):
            roots.add(word[:i])
    
    return min(roots, key=len)

def is_anagram(word):
    counts = [0] * 26
    for c in word:
        counts[ord(c) - ord('a')] += 1
    return all(counts[i] == counts[i-1] for i in range(1, 26))

