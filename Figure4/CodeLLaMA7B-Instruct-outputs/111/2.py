

def histogram(test):
    
    letter_count = {}
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    max_count = 0
    max_letters = []
    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
            max_letters = [letter]
        elif count == max_count:
            max_letters.append(letter)
    return {letter: max_count for letter in max_letters}

