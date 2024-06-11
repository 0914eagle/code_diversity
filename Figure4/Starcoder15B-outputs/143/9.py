def words_in_sentence(sentence):
    
    words = sentence.split()
    return ' '.join(filter(lambda x: is_prime(len(x)), words))


