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
    roman_numerals_reversed = {v: k for k, v in roman_numerals.items()}
    result = ''
    while number > 0:
        for key, value in roman_numerals_reversed.items():
            if number >= key:
                result += value
                number -= key
                break
    return result.lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
