def words_in_sentence(sentence):
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    words = sentence.split()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return " ".join([word for word in words if len(word) in primes])


if __name__ == "__main__":
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))
