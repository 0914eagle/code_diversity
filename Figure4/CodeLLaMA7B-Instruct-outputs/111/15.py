

def histogram(test):
    
    # split the string into a list of individual letters
    letters = test.split()
    # create an empty dictionary to store the results
    results = {}
    # loop through the list of letters
    for letter in letters:
        # if the letter is not in the dictionary, add it with a count of 1
        if letter not in results:
            results[letter] = 1
        # if the letter is already in the dictionary, increment its count
        else:
            results[letter] += 1
    # return the dictionary with the most repetition
    return results


