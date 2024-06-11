def int_to_mini_roman(number):
    
    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    while number > 0:
        for key, value in roman.items():
            if number >= key:
                result += value
                number -= key
    return result.lower()


