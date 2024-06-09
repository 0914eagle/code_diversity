
def get_nearest_fraction(x, y, n):
    min_denominator = float('inf')
    min_numerator = float('inf')
    for denominator in range(1, n+1):
        numerator = round(x*denominator/y)
        if abs(numerator/denominator - x/y) < min_numerator/min_denominator:
            min_numerator = numerator
            min_denominator = denominator
    return str(min_numerator) + '/' + str(min_denominator)

