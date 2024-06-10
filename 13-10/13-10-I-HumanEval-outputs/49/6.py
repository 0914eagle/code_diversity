
def fruit_distribution(s: str, n: int) -> int:
    
    # Initialize the variables
    apples = 0
    oranges = 0
    mangoes = 0
    
    # Split the string into words
    words = s.split()
    
    # Loop through the words and convert the numbers to integers
    for i in range(len(words)):
        if words[i].isdigit():
            if words[i-1] == 'apples':
                apples = int(words[i])
            elif words[i-1] == 'oranges':
                oranges = int(words[i])
            elif words[i-1] == 'mangoes':
                mangoes = int(words[i])
    
    # Calculate the number of mangoes in the basket
    mangoes = n - apples - oranges
    
    # Return the number of mangoes
    return mangoes

