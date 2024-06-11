def words_in_sentence(sentence):
    
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 1:
            continue
        for i in range(2, len(word)):
            if word[i] == word[i - 1]:
                break
            if i == len(word) - 1:
                result.append(word)
                break
    return ' '.join(result)


if __name__ == '__main__':
    print(words_in_sentence("This is a test"))
   