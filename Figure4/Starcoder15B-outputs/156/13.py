def int_to_mini_roman(number):
    
    assert 1 <= number <= 1000, 'Number must be between 1 and 1000'
    roman_numeral = ''
    for numeral, value in ROMAN_NUMERALS:
        while number >= value:
            roman_numeral += numeral
            number -= value
    return roman_numeral.lower()


