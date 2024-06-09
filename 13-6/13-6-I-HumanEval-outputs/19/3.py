
def int_to_mini_roman(number: int) -> str:
    
    roman_numerals = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    result = ''

    while number > 0:
        for value, numeral in zip(roman_values, roman_numerals):
            while number >= value:
                result += numeral
                number -= value

    return result.lower()

