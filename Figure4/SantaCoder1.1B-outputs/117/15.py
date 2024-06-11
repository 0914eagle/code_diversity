def select_words(s, n):
    
    # Write your code here
    words = []
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            words.append(s[i])
    if len(words) == 0:
        return []
    else:
        return words[:n]

