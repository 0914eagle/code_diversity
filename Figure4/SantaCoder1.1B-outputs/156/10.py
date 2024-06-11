def int_to_mini_roman(number):
    
    roman_numeral = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    while number > 0:
        if number >= 1000:
            result += roman_numeral[number // 1000] + roman_numeral[number % 1000]
            number = number % 1000
        else:
            result += roman_numeral[number]
            number = 0
    return result.lower()


