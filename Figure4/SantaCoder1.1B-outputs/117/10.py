def select_words(s, n):
    
    # TODO: Implement this function
    words = []
    for i in range(len(s)):
        if s[i] in "aeiou":
            words.append(s[i])
    if len(words) == 0:
        return []
    if len(words) == 1:
        return [words[0]]
    if len(words) == 2:
        if words[0] == words[1]:
            return [words[0]]
        else:
            return []
    if len(words) == 3:
        if words[0] == words[1] and words[1] == words[2]:
            return [words[0]]
        else:
            return []
    if len(words) == 4:
        if words[0] == words[1] and words[1] == words[2] and words[2] == words[3]:
            return [words[0]]
        else:
            return []
    if len(words) == 5:
        if words[0] == words[1] and words[1] == words[2] and words[2] == words[3] and words[3] == words[4]:
            return [words[0]]
        else:
            return []
    if len(words) == 6:
        if words[0] == words[1] and words[1] == words[2] and words[2] == words[3] and words[3] == words[4] and words[4] == words[5]:
            return [words[0]]
        else:
            return []
    if len(words) == 7:
        if words[0] == words[1] and words[1] == words[2] and words[2] == words[3] and words[3] == words[4] and words[4] == words[5] and words[5] == words[6]:
            return [words[0]]
        else:
            return []
    if len(words) == 8:
        if words[0] == words[1] and words[1] == words[2] and words[2] == words[3] and words[3] == words[4] and words[4] == words[5] and words[5] == words[6] and words[6] == words[7]:
            return [words[0