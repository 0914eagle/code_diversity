def int_to_mini_roman(number):
    
    # Create a dictionary of roman numerals
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }
    # Create a list of roman numerals
    roman_numerals_list = [
        'm',
        'cm',
        'd',
        'cd',
        'c',
        'xc',
        'l',
        'xl',
        'x',
        'ix',
        'v',
        'iv',
        'i'
    ]
    # Create a list of integers
    integers_list = [
        1000,
        900,
        500,
        400,
        100,
        90,
        50,
        40,
        10,
        9,
        5,
        4,
        1
    ]
    # Create a list of roman numerals
    roman_numerals_list_reversed = roman_numerals_list[::-1]
    # Create a list of integers
    integers_list_reversed = integers_list[::-1]
    # Create a list of roman numerals
    roman_numerals_list_reversed_2 = roman_numerals_list_reversed[::-1]
    # Create a list of integers
    integers_list_reversed_2 = integers_list_reversed[::-1]
    # Create a list of roman numerals
    roman_numerals_list_reversed_3 = roman_numerals_list_reversed[::-1]
    # Create a list of integers
    integers_list_reversed_3 = integers_list_reversed[::-1]
    # Create a list of roman numer