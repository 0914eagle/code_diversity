def int_to_mini_roman(number):
    
    roman_numeral = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    return roman_numeral[number]


