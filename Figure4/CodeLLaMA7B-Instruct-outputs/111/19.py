

def histogram(test):
    
    letter_count = {}
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    max_count = max(letter_count.values())
    result = {}
    for letter, count in letter_count.items():
        if count == max_count:
            result[letter] = count
    return result


