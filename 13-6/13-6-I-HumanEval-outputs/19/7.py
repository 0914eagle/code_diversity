
def int_to_mini_roman(number: int) -> str:
    
    roman_numerals = ['m', 'd', 'c', 'l', 'x', 'v', 'i']
    roman_values = [1000, 500, 100, 50, 10, 5, 1]
    result = ""

    for value, numeral in zip(roman_values, roman_numerals):
        count = int(number / value)
        result += numeral * count
        number %= value

    return result.lower()

