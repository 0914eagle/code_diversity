
def int_to_mini_roman(number: int) -> str:
    
    roman_numerals = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    tens = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']

    hundreds_digit = number // 100
    tens_digit = (number % 100) // 10
    ones_digit = number % 10

    return hundreds[hundreds_digit] + tens[tens_digit] + ones[ones_digit]

