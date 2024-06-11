


def change_base(x: int, base: int):
    
    # convert the input number x to a string in base 10
    x_str = str(x)
    
    # create a dictionary to map digits in base 10 to digits in the target base
    base_map = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f'}
    
    # create an empty string to store the output
    result = ''
    
    # loop through the digits of the input number in base 10
    for digit in x_str:
        # convert each digit to the target base and add it to the output string
        result += base_map[digit]
    
    # return the output string
    return result


