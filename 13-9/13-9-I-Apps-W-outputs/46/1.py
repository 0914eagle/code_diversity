
def solve(n):
    quasibinary_numbers = []
    while n > 0:
        quasibinary_numbers.append(str(n % 3))
        n //= 3
    quasibinary_numbers.reverse()
    return " ".join(quasibinary_numbers)

