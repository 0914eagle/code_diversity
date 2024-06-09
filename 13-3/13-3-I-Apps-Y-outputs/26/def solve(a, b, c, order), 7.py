
def solve(a, b, c, order):
    # Convert the input strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    
    # Create a dictionary to map the letters to the integers
    letter_to_num = {'A': a, 'B': b, 'C': c}
    
    # Create a list to store the integers in the desired order
    num_list = []
    
    # Iterate through the order string and add the corresponding integer to the list
    for letter in order:
        num_list.append(letter_to_num[letter])
    
    # Return the list as a string with spaces between the integers
    return ' '.join(str(num) for num in num_list)

