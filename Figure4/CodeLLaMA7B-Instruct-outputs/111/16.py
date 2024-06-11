

def histogram(test):
    
    # Your code here
    letter_count = {}
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    max_count = 0
    for letter, count in letter_count.items():
        if count > max_count:
            max_count = count
    result = {}
    for letter, count in letter_count.items():
        if count == max_count:
            result[letter] = count
    return result
