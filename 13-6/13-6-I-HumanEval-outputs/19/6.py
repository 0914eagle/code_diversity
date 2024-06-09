
def int_to_mini_roman(number: int) -> str:
    
    roman_numerals = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    result = ''

    for value in roman_values:
        if number // value > 0:
            result += roman_numerals[roman_values.index(value)] * (number // value)
            number %= value

    return result.lower()

