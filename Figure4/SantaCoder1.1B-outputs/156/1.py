def int_to_mini_roman(number):
    
    roman_numerals = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'l',
        50: 'c',
        90: 'd',
        100: 'm'
    }
    roman_numerals_reversed = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }
    roman_numerals_reversed_reversed = {
        'l': 5,
        'c': 10,
        'd': 50,
        'm': 100
    }
    roman_numerals_reversed_reversed_reversed = {
        'x': 10,
        'v': 5,
        'i': 1
    }
    roman_numerals_reversed_reversed_reversed_reversed = {
        'c': 10,
        'd': 50,
        'm': 100
    }
    if number < 1 or number > 3999:
        raise ValueError('Number out of range')
    if number == 1:
        return 'i'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 9:
        return 'ix'
    elif number == 10:
        return 'x'
    elif number == 40:
        return 'l'
    elif number == 50:
        return 'c'
    elif number == 90:
        return 'd'
    elif number == 100:
        return 'm'
    else:
        roman_numeral = roman_numerals[number]
        roman_numeral_reversed = roman_numerals_reversed[roman_numeral]
        roman_numeral_reversed_reversed = roman_numerals_reversed_reversed[roman_numeral]
        roman_numeral_reversed_reversed_reversed = roman_numerals_reversed_reversed_reversed[roman_numeral]
        roman_numeral_reversed_reversed_reversed_reversed =