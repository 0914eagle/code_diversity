

def histogram(test):
    
    # Split the input string into a list of individual letters
    letters = test.split()
    # Create an empty dictionary to store the results
    results = {}
    # Iterate over the list of letters and increment the count for each letter
    for letter in letters:
        if letter in results:
            results[letter] += 1
        else:
            results[letter] = 1
    # Find the letter(s) with the highest count
    highest_count = max(results.values())
    # Create a list to store the letters with the highest count
    highest_letters = []
    # Iterate over the results dictionary and append letters with the highest count to the list
    for letter, count in results.items():
        if count == highest_count:
            highest_letters.append(letter)
    # Return the dictionary with the highest count and the corresponding letters
    return {highest_count: highest_letters}


