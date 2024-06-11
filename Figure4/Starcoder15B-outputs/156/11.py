def int_to_mini_roman(number):
    
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_numeral = ""
    for numeral, value in _ROMAN_NUMERALS:
        while number >= value:
            roman_numeral += numeral
            number -= value

    return roman_numeral.lower()


