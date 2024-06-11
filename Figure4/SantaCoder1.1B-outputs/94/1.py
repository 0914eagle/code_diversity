def skjkasdkd(lst):
    
    lst = sorted(lst)
    max_prime = lst[-1]
    sum_of_digits = 0
    for i in range(len(lst)):
        if lst[i] > max_prime:
            break
        sum_of_digits += lst[i]
    return sum_of_digits


