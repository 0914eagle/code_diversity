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
    roman_numerals_reversed_inv = {
        'i': 9,
        'v': 4,
        'x': 90,
        'l': 40,
        'c': 10,
        'd': 400,
        'm': 100
    }
    roman_numerals_inv = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }
    roman_numerals_inv_reversed = {
        'i': 9,
        'v': 4,
        'x': 90,
        'l': 40,
        'c': 10,
        'd': 400,
        'm': 100
    }
    roman_numerals_inv_reversed_inv = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }
    roman_numerals_inv_inv = {
        'i': 9,
        'v': 4,
        'x': 90,
        'l': 40,
        'c': 10,
        'd': 400,
        'm': 100
    }
    roman_numerals_inv_inv_inv = {
        'i': 1,
        'v