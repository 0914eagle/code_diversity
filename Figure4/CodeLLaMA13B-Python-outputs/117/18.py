def select_words(s, n):
    
    # your code here
    words = s.split()
    result = []
    for word in words:
        if word.count(word[0]) == n:
            result.append(word)
    return result


if