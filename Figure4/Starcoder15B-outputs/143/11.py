def words_in_sentence(sentence):
    
    return ' '.join(filter(lambda word: is_prime(len(word)), sentence.split()))


