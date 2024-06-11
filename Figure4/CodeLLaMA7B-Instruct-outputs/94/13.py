


def skjkasdkd(lst):
    

    # Find the largest prime number in the list
    prime_numbers = []
    for i in lst:
        if is_prime(i):
            prime_numbers.append(i)

    largest_prime = max(prime_numbers)

    # Return the sum of the digits of the largest prime number
    return sum(str(largest_prime))


def is_prime(n):
    if n
