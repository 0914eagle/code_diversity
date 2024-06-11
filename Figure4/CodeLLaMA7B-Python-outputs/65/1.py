def circular_shift(x, shift):
    
    # Base case
    if x < 10:
        return str(x)
    # Recursive case
    else:
        # Get the last digit
        last_digit = x % 10
        # Get the rest of the number
        rest = x // 10
        # Get the last digit of the rest
        last_digit_rest = rest % 10
        # Get the rest of the rest
        rest_rest = rest // 10
        # If the shift is greater than the number of digits, reverse the number
        if shift >= len(str(x)):
            return str(last_digit_rest) + str(last_digit) + str(rest_rest)
        # Otherwise, shift the digits
        else:
            return str(last_digit_rest) + str(rest_rest) + str(last_digit)


if