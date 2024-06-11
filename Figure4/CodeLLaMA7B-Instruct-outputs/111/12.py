

def histogram(test):
    
    # split the string into a list of individual letters
    letters = test.split()
    # create an empty dictionary to store the results
    results = {}
    # loop through the list of letters
    for letter in letters:
        # if the letter is already in the dictionary, increment its count
        if letter in results:
            results[letter] += 1
        # otherwise, add the letter to the dictionary with a count of 1
        else:
            results[letter] = 1
    # sort the dictionary by value (descending)
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # return the dictionary
    return sorted_results


