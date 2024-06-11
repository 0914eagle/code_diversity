def words_in_sentence(sentence):
    
    # O(n) time | O(n) space
    words = sentence.split()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primes_set = set(primes)
    result = []
    for word in words:
        if len(word) in primes_set:
            result.append(word)
    return " ".join(result)
