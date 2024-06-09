
def convert_to_exponential(x):
    # Convert the input to a string
    x_str = str(x)
    
    # Find the index of the decimal point
    decimal_index = x_str.find(".")
    
    # If the decimal point is not found, the number is an integer
    if decimal_index == -1:
        return x_str + "E0"
    
    # Extract the integer part of the number
    integer_part = x_str[:decimal_index]
    
    # Extract the fractional part of the number
    fractional_part = x_str[decimal_index+1:]
    
    # Check if the fractional part is all zeroes
    if fractional_part.strip("0") == "":
        return integer_part + "E0"
    
    # Find the exponent
    exponent = len(fractional_part) - 1
    
    # Return the exponential notation
    return integer_part + "." + fractional_part + "E" + str(exponent)

def main():
    x = input("Enter a positive decimal number: ")
    print(convert_to_exponential(x))

if __name__ == '__main__':
    main()

