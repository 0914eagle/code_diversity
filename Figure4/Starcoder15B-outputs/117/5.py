def select_words(s, n):
    
    # Your code here
    if s == "":
        return []
    else:
        words = s.split()
        result = []
        for word in words:
            if len(word) - len(word.strip(vowels)) == n:
                result.append(word)
        return result

