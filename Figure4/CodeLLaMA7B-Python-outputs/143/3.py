def words_in_sentence(sentence):
    
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 1:
            result.append(word)
        elif len(word) > 1:
            for i in range(1, len(word)):
                if len(word) % i == 0:
                    result.append(word)
                    break
    return result


if __name__ == "__main__":
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
