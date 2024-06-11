def words_in_sentence(sentence):
    
    result = []
    for word in sentence.split():
        is_prime = True
        for i in range(2, len(word)):
            if word[0] == word[i] and word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
                is_prime = False
                break
        if is_prime:
            result.append(word)
    return ' '.join(result)


if