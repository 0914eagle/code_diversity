
def get_quasibinary_representation(n):
    quasibinary_numbers = []
    while n > 0:
        quasibinary_numbers.append(str(n % 2))
        n //= 2
    return " ".join(quasibinary_numbers[::-1])

