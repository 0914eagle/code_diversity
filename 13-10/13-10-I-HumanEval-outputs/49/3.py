
def fruit_distribution(s: str, n: int) -> int:
    
    # Remove any leading or trailing whitespace
    s = s.strip()
    
    # Split the input string into a list of words
    words = s.split()
    
    # Initialize variables to keep track of the number of apples, oranges, and mangoes
    num_apples = 0
    num_oranges = 0
    num_mangoes = 0
    
    # Iterate through the list of words
    for word in words:
        # Check if the word is a number
        if word.isdigit():
            # If it is, convert it to an integer and add it to the total number of fruits
            num_fruits += int(word)
        # Check if the word is "apple"
        elif word.lower() == "apple":
            # If it is, add 1 to the number of apples
            num_apples += 1
        # Check if the word is "orange"
        elif word.lower() == "orange":
            # If it is, add 1 to the number of oranges
            num_oranges += 1
        # Check if the word is "mango"
        elif word.lower() == "mango":
            # If it is, add 1 to the number of mangoes
            num_mangoes += 1
    
    # Calculate the number of mangoes in the basket
    num_mangoes = n - (num_apples + num_oranges)
    
    # Return the number of mangoes
    return num_mangoes

