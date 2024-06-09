
def solve(a, b, c, order):
    # Convert the input strings to integers
    a = int(a)
    b = int(b)
    c = int(c)
    
    # Create a dictionary to map the letters to the integers
    letter_to_num = {'A': a, 'B': b, 'C': c}
    
    # Use the dictionary and the desired order to rearrange the integers
    nums = [letter_to_num[letter] for letter in order]
    
    # Return the rearranged integers
    return " ".join(str(num) for num in nums)

