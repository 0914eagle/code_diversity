def words_in_sentence(sentence):
    
    words = sentence.split()
    return ' '.join(filter(lambda word: is_prime(len(word)), words))


