
def fruit_distribution(s: str, n: int) -> int:
    
    # split the string into a list of words
    words = s.split()
    # initialize variables to keep track of the number of apples and oranges
    num_apples = 0
    num_oranges = 0
    # loop through the list of words and check if the current word is "apple" or "orange"
    for word in words:
        if word == "apple":
            num_apples += 1
        elif word == "orange":
            num_oranges += 1
    # calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples - num_oranges
    return num_mangoes

