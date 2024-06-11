def int_to_mini_roman(number):
    
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numeral = ''
    roman_numeral += 'm' * (number // 1000)
    roman_numeral += 'd' * ((number % 1000) // 500)
    roman_numeral += 'c' * ((number % 500) // 100)
    roman_numeral += 'l' * ((number % 100) // 50)
    roman_numeral += 'x' * ((number % 50) // 10)
    roman_numeral += 'v' * ((number % 10) // 5)
    roman_numeral += 'i' * (number % 5)
    return roman_numeral.lower()


