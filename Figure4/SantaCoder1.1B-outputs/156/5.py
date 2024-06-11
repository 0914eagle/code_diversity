def int_to_mini_roman(number):
    
    roman_numerals = {
        1: 'i',
        4: 'v',
        5: 'vi',
        9: 'x',
        10: 'xi',
        40: 'l',
        50: 'lx',
        90: 'c',
        100: 'xc',
        400: 'xl',
        500: 'lxx',
        900: 'cc',
        1000: 'ccc',
    }
    result = ''
    while number > 0:
        for key, value in roman_numerals.items():
            if number >= key:
                result += value
                number -= key
                break
    return result.lower()


