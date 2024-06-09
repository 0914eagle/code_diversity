
def fruit_distribution(s: str, n: int) -> int:
    
    # Initialize the number of mango fruits to 0
    mango_fruits = 0
    
    # Split the input string into a list of words
    words = s.split()
    
    # Iterate over the list of words
    for word in words:
        # Check if the word is a number
        if word.isdigit():
            # If the word is a number, add it to the total number of fruits
            n -= int(word)
    
    # The number of mango fruits is the difference between the total number of fruits and the number of oranges and apples
    mango_fruits = n
    
    # Return the number of mango fruits
    return mango_fruits

