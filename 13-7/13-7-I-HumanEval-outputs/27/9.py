
def fruit_distribution(s: str, n: int) -> int:
    
    # split the string into a list of words
    words = s.split()
    # initialize variables to store the number of apples and oranges
    num_apples = 0
    num_oranges = 0
    # loop through the list of words and extract the number of apples and oranges
    for word in words:
        if 'apple' in word:
            num_apples = int(word.replace('apples', ''))
        elif 'orange' in word:
            num_oranges = int(word.replace('oranges', ''))
    # calculate the total number of fruits
    total_fruits = num_apples + num_oranges
    # return the number of mango fruits
    return n - total_fruits

