def int_to_mini_roman(number):
    
    roman_numeral = {
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
    roman_numeral_list = list(roman_numeral.values())
    roman_numeral_list.sort()
    roman_numeral_list.reverse()
    return ''.join(roman_numeral_list[number - 1])


