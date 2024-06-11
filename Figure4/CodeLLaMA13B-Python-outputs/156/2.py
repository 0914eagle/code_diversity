def int_to_mini_roman(number):
    
    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000")

    roman_numerals = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    ]

    result = ""
    for numeral, roman in roman_numerals:
        while number >= numeral:
            result += roman
            number -= numeral

    return result.lower()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
