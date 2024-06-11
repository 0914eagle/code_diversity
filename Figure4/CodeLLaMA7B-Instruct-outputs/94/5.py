


def skjkasdkd(lst):
    

    # Find the largest prime value in the list
    prime_values = []
    for i in lst:
        if is_prime(i):
            prime_values.append(i)

    # Return the sum of the digits of the largest prime value
    if len(prime_values) == 0:
        return 0
    else:
        return sum(str(prime_values[-1]))


def
