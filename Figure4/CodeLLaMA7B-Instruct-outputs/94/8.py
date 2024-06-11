


def skjkasdkd(lst):
    

    # Find the largest prime value in the list
    prime_values = []
    for i in lst:
        if is_prime(i):
            prime_values.append(i)

    # Return the sum of the digits of the largest prime value
    if prime_values:
        return sum(str(prime_values[-1]))
    else:
        return 0


def is_prime(n):
