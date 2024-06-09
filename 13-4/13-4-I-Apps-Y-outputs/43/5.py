
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    words = []
    for i in range(1, len(word) // 2 + 1):
        if word[:i] == word[len(word) - i:]:
            words.append(word[:i])
    
    if len(words) == 0:
        return -1
    
    return min(words, key=len)

