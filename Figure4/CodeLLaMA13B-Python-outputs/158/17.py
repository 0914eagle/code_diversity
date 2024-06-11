def find_max(words):
    
    max_word = ""
    max_chars = 0
    for word in words:
        if len(word) > max_chars:
            max_word = word
            max_chars = len(word)
        elif len(word) == max_chars:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == "__main__":
    print(find_max(["name", "of", "string"]))
    print(find_max(["name", "enam", "game"]))
    print(find_max(["aaaaaaa", "bb", "cc"]))
