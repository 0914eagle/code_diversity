
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    for i in range(1, len(word) // 2 + 1):
        if word[:i] == word[len(word) - i:] and is_anagram(word[:i], word[len(word) - i:]):
            return word[:i]
    
    return -1

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    count = [0] * 26
    
    for c in word1:
        count[ord(c) - ord('a')] += 1
    
    for c in word2:
        count[ord(c) - ord('a')] -= 1
        if count[ord(c) - ord('a')] < 0:
            return False
    
    return True

word = input()
print(is_multigram(word))

