def skjkasdkd(lst):
    
    max_prime = 0
    for i in lst:
        if is_prime(i):
            if i > max_prime:
                max_prime = i
    return sum_of_digits(max_prime)


