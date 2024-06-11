def int_to_mini_roman(number):
    
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numeral = ''
    while number >= 1000:
        roman_numeral += 'm'
        number -= 1000
    while number >= 900:
        roman_numeral += 'cm'
        number -= 900
    while number >= 500:
        roman_numeral += 'd'
        number -= 500
    while number >= 400:
        roman_numeral += 'cd'
        number -= 400
    while number >= 100:
        roman_numeral += 'c'
        number -= 100
    while number >= 90:
        roman_numeral += 'xc'
        number -= 90
    while number >= 50:
        roman_numeral += 'l'
        number -= 50
    while number >= 40:
        roman_numeral += 'xl'
        number -= 40
    while number >= 10:
        roman_numeral += 'x'
        number -= 10
    while number >= 9:
        roman_numeral += 'ix'
        number -= 9
    while number >= 5:
        roman_numeral += 'v'
        number -= 5
    while number >= 4:
        roman_numeral += 'iv'
        number -= 4
    while number >= 1:
        roman_numeral += 'i'
        number -= 1

    return roman_numeral.lower()


