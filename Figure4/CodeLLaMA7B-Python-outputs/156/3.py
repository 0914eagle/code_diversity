def int_to_mini_roman(number):
    
    # Your code here
    roman_numerals = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    roman_numerals_values = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }

    roman_numeral = ''

    while number > 0:
        for key, value in roman_numerals.items():
            if number >= key:
                roman_numeral += value
                number -= key
                break

    return roman_numeral


