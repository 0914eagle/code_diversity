
def words_in_sentence(sentence: str) -> str:
    

    prime_words = []
    for word in sentence.split():
        if is_prime(len(word)):
            prime_words.append(word)
    return " ".join(prime_words)

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

