
def int_to_mini_roman(number: int) -> str:
    
    roman_numerals = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    roman_numeral_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    result = ''
    while number > 0:
        for value, numeral in roman_numeral_map.items():
            if number >= value:
                result += numeral
                number -= value
                break
    return result.lower()

