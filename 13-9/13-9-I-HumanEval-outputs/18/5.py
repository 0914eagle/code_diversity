
def words_in_sentence(sentence: str) -> str:
    

    # split the sentence into a list of words
    words = sentence.split()

    # initialize an empty string to store the result
    result = ""

    # iterate over the words in the sentence
    for word in words:
        # check if the length of the word is a prime number
        if is_prime(len(word)):
            # if it is, add it to the result string
            result += word + " "

    # remove the trailing space from the result string
    return result.strip()

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

