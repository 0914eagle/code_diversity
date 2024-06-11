def histogram(test):
    
    # Your code here
    # Create a dictionary to store the letters and their counts
    letter_counts = {}

    # Split the string into a list of letters
    letters = test.split()

    # Iterate over the list of letters
    for letter in letters:
        # Check if the letter is already in the dictionary
        if letter in letter_counts:
            # If it is, increment the count
            letter_counts[letter] += 1
        else:
            # If it isn't, add it to the dictionary with a count of 1
            letter_counts[letter] = 1

    # Find the maximum count
    max_count = max(letter_counts.values())

    # Create a list to store the letters with the maximum count
    max_letters = []

    # Iterate over the dictionary
    for letter, count in letter_counts.items():
        # If the count is equal to the maximum count, add the letter to the list
        if count == max_count:
            max_letters.append(letter)

    # Return a dictionary with the letters and their counts
    return {letter: count for letter, count in letter_counts.items() if count in max_letters}


print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
/Python/Python_OOP/Python OOP 14.py
#