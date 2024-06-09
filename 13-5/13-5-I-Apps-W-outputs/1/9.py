
def get_exponential_notation(x):
    # Convert x to a string
    x_str = str(x)
    
    # Find the index of the decimal point
    decimal_index = x_str.find(".")
    
    # If the decimal point is not found, return the input number
    if decimal_index == -1:
        return x_str
    
    # Extract the digits before and after the decimal point
    before_decimal = x_str[:decimal_index]
    after_decimal = x_str[decimal_index+1:]
    
    # If the number is an integer, remove the decimal point
    if after_decimal == "0":
        return before_decimal
    
    # If the number is not an integer, add the decimal point back
    else:
        return before_decimal + "." + after_decimal

def main():
    x = input()
    print(get_exponential_notation(x))

if __name__ == '__main__':
    main()

