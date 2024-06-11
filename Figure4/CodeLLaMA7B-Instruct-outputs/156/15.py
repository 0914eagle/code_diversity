

def int_to_mini_roman(number):
    
    num_dict = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xcx',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }

    roman_numeral = ''
    for values in sorted(num_dict.items(), reverse=True):
        div, num = values
        while number >= div:
            roman_numeral += num
            number -= div

    return roman_numeral


