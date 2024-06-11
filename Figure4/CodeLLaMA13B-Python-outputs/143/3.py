def words_in_sentence(sentence):
    
    result = []
    for word in sentence.split():
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


