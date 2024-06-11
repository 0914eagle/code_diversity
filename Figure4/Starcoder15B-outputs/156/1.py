def int_to_mini_roman(number):
    
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numerals = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    roman_numeral_string = ''
    for numeral in sorted(roman_numerals.keys(), reverse=True):
        while number >= numeral:
            roman_numeral_string += roman_numerals[numeral]
            number -= numeral
    return roman_numeral_string.lower()


