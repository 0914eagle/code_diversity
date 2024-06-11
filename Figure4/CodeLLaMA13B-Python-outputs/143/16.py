def words_in_sentence(sentence):
    
    words = sentence.split()
    result = []
    for word in words:
        is_prime = True
        for i in range(2, len(word)):
            if word[0] == word[i] and word[0] != 'a' and word[0] != 'i' and word[0] != 'e':
                is_prime = False
                break
        if is_prime:
            result.append(word)
    return ' '.join(result)


if __name__ == '__main__':
    print