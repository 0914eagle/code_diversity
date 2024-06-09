
def f1(x):
    # convert x to a string
    x_str = str(x)
    
    # find the decimal point in the string
    decimal_point_index = x_str.find(".")
    
    # if the decimal point is not found, return the input number
    if decimal_point_index == -1:
        return x
    
    # get the integer part of the number
    integer_part = x_str[:decimal_point_index]
    
    # get the fractional part of the number
    fractional_part = x_str[decimal_point_index+1:]
    
    # convert the fractional part to an integer
    fractional_part_int = int(fractional_part)
    
    # calculate the exponent
    exponent = len(fractional_part) - 1
    
    # convert the integer part to a float
    float_part = float(integer_part)
    
    # calculate the final result
    result = float_part * (10 ** exponent)
    
    # return the result
    return result

def f2(x):
    # convert x to a string
    x_str = str(x)
    
    # find the decimal point in the string
    decimal_point_index = x_str.find(".")
    
    # if the decimal point is not found, return the input number
    if decimal_point_index == -1:
        return x
    
    # get the integer part of the number
    integer_part = x_str[:decimal_point_index]
    
    # get the fractional part of the number
    fractional_part = x_str[decimal_point_index+1:]
    
    # convert the fractional part to an integer
    fractional_part_int = int(fractional_part)
    
    # calculate the exponent
    exponent = len(fractional_part) - 1
    
    # convert the integer part to a float
    float_part = float(integer_part)
    
    # calculate the final result
    result = float_part * (10 ** exponent)
    
    # return the result
    return result

if __name__ == '__main__':
    x = float(input())
    print(f1(x))
    print(f2(x))

