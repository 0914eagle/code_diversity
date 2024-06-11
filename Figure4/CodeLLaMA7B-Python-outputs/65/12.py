def circular_shift(x, shift):
    
    if shift == 0:
        return str(x)
    if x == 0:
        return '0'
    if x < 0:
        x = -x
        sign = '-'
    else:
        sign = ''
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = x // 10
    if shift > len(digits):
        return sign + ''.join(map(str, reversed(digits)))
    else:
        return sign + ''.join(map(str, digits[shift:] + digits[:shift]))


if