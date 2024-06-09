
def is_divine_digit(number, base, divine_digit):
    return str(number)[-1] == str(divine_digit)

def get_divine_digits(denominations, base):
    divine_digits = set()
    for denomination in denominations:
        for i in range(base):
            if is_divine_digit(denomination, base, i):
                divine_digits.add(i)
    return list(divine_digits)

def solve(denominations, base):
    divine_digits = get_divine_digits(denominations, base)
    return len(divine_digits), sorted(divine_digits)

