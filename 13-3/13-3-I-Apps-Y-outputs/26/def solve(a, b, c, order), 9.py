
def solve(a, b, c, order):
    # Convert the input strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    
    # Create a dictionary to map the letters to the integers
    letter_to_num = {"A": a, "B": b, "C": c}
    
    # Create a list to store the integers in the desired order
    result = []
    
    # Iterate through the order string and add the corresponding integer to the result list
    for letter in order:
        result.append(letter_to_num[letter])
    
    # Return the result list as a string separated by spaces
    return " ".join(map(str, result))

