def int_to_mini_roman(number):
    
    roman_numerals = {
        1: 'i',
        4: 'v',
        5: 'x',
        9: 'm',
        10: 'c',
        40: 'iv',
        50: 'xv',
        90: 'mc',
        100: 'cm'
    }
    roman_numerals_lower = {v.lower(): k for k, v in roman_numerals.items()}
    roman_numerals_lower[100] = 'l'
    roman_numerals_lower[400] = 'xl'
    roman_numerals_lower[900] = 'cd'
    roman_numerals_lower[1000] = 'd'
    roman_numerals_lower[4000] = 'cd'
    roman_numerals_lower[9000] = 'cm'
    roman_numerals_lower[10000] = 'm'
    roman_numerals_lower[40000] = 'cd'
    roman_numerals_lower[90000] = 'dm'
    roman_numerals_lower[100000] = 'cm'
    roman_numerals_lower[400000] = 'cd'
    roman_numerals_lower[900000] = 'dm'
    roman_numerals_lower[1000000] = 'm'
    roman_numerals_lower[4000000] = 'cd'
    roman_numerals_lower[9000000] = 'dm'
    roman_numerals_lower[10000000] = 'm'
    roman_numerals_lower[40000000] = 'cd'
    roman_numerals_lower[90000000] = 'dm'
    roman_numerals_lower[100000000] = 'm'
    roman_numerals_lower[400000000] = 'cd'
    roman_numerals_lower[90000000