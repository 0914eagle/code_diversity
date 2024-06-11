def find_max(words):
    
    if not words:
        return ""
    max_word = words[0]
    max_count = 0
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == "__main__":
    print