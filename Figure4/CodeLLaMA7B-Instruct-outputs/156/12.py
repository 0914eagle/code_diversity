

def int_to_mini_roman(number):
    
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_numeral = ''
    while number > 0:
        for i in range(len(values)):
            if number >= values[i]:
                number -= values[i]
                roman_numeral += roman_numerals[i]
                break

    return roman_numeral


