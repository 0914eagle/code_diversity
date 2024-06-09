
def is_multigram(word):
    if len(word) < 3:
        return -1
    
    # Check if the word is a permutation of a shorter word
    for i in range(1, len(word) // 2 + 1):
        if word[:i] == word[len(word) - i:] and is_anagram(word[:i]):
            return word[:i]
    
    # Check if the word is a concatenation of two or more anagrams
    for i in range(1, len(word)):
        if is_anagram(word[:i]) and is_anagram(word[i:]):
            return word[:i]
    
    return -1

def is_anagram(word):
    return sorted(word) == sorted(word[::-1])

