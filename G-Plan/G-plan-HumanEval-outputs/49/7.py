
def int_to_mini_roman(number: int) -> str:
    roman_mapping = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
        50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    
    result = ""
    for value, symbol in roman_mapping.items():
        while number >= value:
            result += symbol
            number -= value
    
    return result

# Read input
number = int(input())
# Output result
print(int_to_mini_roman(number))