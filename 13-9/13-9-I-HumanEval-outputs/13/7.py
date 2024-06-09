
def fruit_distribution(s: str, n: int) -> int:
    
    # Initialize the count of mango fruits to 0
    mango_count = 0
    
    # Split the input string into a list of words
    words = s.split()
    
    # Iterate over the list of words
    for word in words:
        # Check if the word is a number
        if word.isdigit():
            # If it is a number, increment the count of mango fruits
            mango_count += 1
    
    # Return the count of mango fruits
    return mango_count

