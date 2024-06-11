def words_in_sentence(sentence):
    
    words = sentence.split()
    words_prime = []
    for word in words:
        if len(word) > 1:
            words_prime.append(word)
    return " ".join(words_prime)


if