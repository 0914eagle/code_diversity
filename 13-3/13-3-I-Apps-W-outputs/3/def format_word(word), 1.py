
def format_word(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    formatted_word = ""
    for i in range(len(word)):
        if word[i] in vowels:
            if i + 1 < len(word) and word[i + 1] == word[i]:
                if word[i] in ["e", "o"] and i + 2 < len(word) and word[i + 2] == word[i]:
                    formatted_word += word[i]
                    i += 2
                else:
                    i += 1
            else:
                formatted_word += word[i]
        else:
            formatted_word += word[i]
    return formatted_word

