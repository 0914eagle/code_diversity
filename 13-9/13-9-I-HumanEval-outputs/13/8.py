
def fruit_distribution(s: str, n: int) -> int:
    
    # split the string into a list of words
    words = s.split()
    # initialize variables to keep track of the number of apples and oranges
    num_apples = 0
    num_oranges = 0
    # loop through the list of words
    for word in words:
        # check if the word is a number
        if word.isdigit():
            # if the word is a number, add it to the total number of fruits
            n += int(word)
        # check if the word is "apples"
        elif word == "apples":
            # if the word is "apples", add the number of apples to the total number of fruits
            num_apples += int(words[0])
        # check if the word is "oranges"
        elif word == "oranges":
            # if the word is "oranges", add the number of oranges to the total number of fruits
            num_oranges += int(words[1])
    # calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples - num_oranges
    return num_mangoes

