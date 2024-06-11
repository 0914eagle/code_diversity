def int_to_mini_roman(number):
    
    roman_numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    roman_numeral = ''
    while number > 0:
        for key, value in roman_numerals.items():
            if number >= key:
                roman_numeral += value
                number -= key
                break
    return roman_numeral.lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
