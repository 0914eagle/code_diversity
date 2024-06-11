def int_to_mini_roman(number):
    
    roman = ''
    while number > 0:
        if number >= 1000:
            roman += 'l'
            number -= 1000
        elif number >= 900:
            roman += 'c'
            number -= 900
        elif number >= 500:
            roman += 'd'
            number -= 500
        elif number >= 400:
            roman += 'm'
            number -= 400
        elif number >= 100:
            roman += 'x'
            number -= 100
        elif number >= 90:
            roman += 'v'
            number -= 90
        elif number >= 50:
            roman += 'i'
            number -= 50
        elif number >= 40:
            roman += 'i'
            number -= 40
        elif number >= 10:
            roman += 'i'
            number -= 10
        elif number >= 9:
            roman += 'i'
            number -= 9
        elif number >= 5:
            roman += 'v'
            number -= 5
        elif number >= 4:
            roman += 'v'
            number -= 4
        elif number >= 1:
            roman += 'v'
            number -= 1
        else:
            roman += 'i'
            number -= 1
    return roman.lower()


