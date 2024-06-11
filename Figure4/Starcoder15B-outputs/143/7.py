def words_in_sentence(sentence):
    
    return ' '.join([word for word in sentence.split() if is_prime(len(word))])


