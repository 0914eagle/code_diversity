def select_words(s, n):
    
    # Write your code here
    words = []
    for i in range(len(s)):
        if s[i] == " ":
            continue
        if len(s[i:]) == n:
            words.append(s[i:])
    return words

