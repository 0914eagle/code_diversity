
def f1(n, word):
    # Your code here
    return "DA" if is_winning_word(word) else "NE"

def f2(n, word):
    # Your code here
    return get_most_beautiful_word(word)

def is_winning_word(word):
    # Check if the word is a valid word
    if not is_valid_word(word):
        return False
    
    # Check if the word is the most beautiful word
    if is_most_beautiful_word(word):
        return True
    
    # Recursively check if the next word is a winning word
    return is_winning_word(get_next_word(word))

def is_valid_word(word):
    # Check if the word is a valid word
    return word in valid_words

def is_most_beautiful_word(word):
    # Check if the word is the most beautiful word
    return word > most_beautiful_word

def get_next_word(word):
    # Get the next word by removing the rightmost letter and appending it to the end of the word
    return word[:-1] + word[-1]

def get_most_beautiful_word(word):
    # Get the most beautiful word by removing the rightmost letter and appending it to the end of the word
    # until a valid word is reached
    while not is_valid_word(word):
        word = word[:-1] + word[-1]
    return word

if __name__ == '__main__':
    n = int(input())
    word = input()
    print(f1(n, word))
    print(f2(n, word))

