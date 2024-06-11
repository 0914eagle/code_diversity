def find_max(words):
    
    max_word = ""
    max_characters = 0
    for word in words:
        if len(word) > max_characters:
            max_characters = len(word)
            max_word = word
        elif len(word) == max_characters:
            if word < max_word:
                max_word = word
    return max_word


if __name__ == "__main__":
    print(find_max(["name", "of", "string"]))
