
def words_in_sentence(sentence: str) -> str:
    
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    words = sentence.split()
    prime_word_indices = []
    for i, word in enumerate(words):
        if len(word) in prime_numbers:
            prime_word_indices.append(i)
    return ' '.join([words[i] for i in prime_word_indices])

