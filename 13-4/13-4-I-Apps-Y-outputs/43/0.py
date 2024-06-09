
def is_multigram(word):
    if len(word) <= 2:
        return -1
    
    words = []
    for i in range(1, len(word) // 2 + 1):
        if len(word) % i == 0:
            words.append(word[:i])
    
    for word1 in words:
        if all(word1 in word for word2 in words if word1 != word2):
            return word1
    
    return -1

