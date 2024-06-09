
def convert_to_exponential(x):
    # Convert the input to a string
    x_str = str(x)
    
    # Find the index of the decimal point
    decimal_index = x_str.find(".")
    
    # If the decimal point is not found, return the input as is
    if decimal_index == -1:
        return x_str
    
    # Extract the digits before and after the decimal point
    before_decimal = x_str[:decimal_index]
    after_decimal = x_str[decimal_index+1:]
    
    # If the digits after the decimal point are all zeroes, return the input as is
    if after_decimal.replace("0", "") == "":
        return x_str
    
    # Find the power of 10 to which the number needs to be raised to make the digits after the decimal point equal to 1
    power = len(after_decimal) - 1
    
    # Convert the number to the "simple exponential notation"
    return f"{before_decimal}.{after_decimal}E{power}"

def main():
    x = input("Enter a positive decimal number: ")
    print(convert_to_exponential(x))

if __name__ == '__main__':
    main()

