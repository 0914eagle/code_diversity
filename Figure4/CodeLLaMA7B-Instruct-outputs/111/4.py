

def histogram(test):
    
    # split the string into a list of individual letters
    letters = test.split()
    # create an empty dictionary to store the results
    results = {}
    # loop through the list of letters and increment the count for each letter
    for letter in letters:
        if letter in results:
            results[letter] += 1
        else:
            results[letter] = 1
    # find the letter(s) with the highest count
    highest_count = max(results.values())
    # create a new dictionary with the letters that have the highest count
    highest_letters = {letter: count for letter, count in results.items() if count == highest_count}
    return highest_letters


