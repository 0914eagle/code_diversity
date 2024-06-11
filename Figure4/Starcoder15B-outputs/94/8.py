def skjkasdkd(lst):
    
    lst = [i for i in lst if i > 0]
    if len(lst) == 0:
        return 0
    lst = [i for i in lst if is_prime(i)]
    if len(lst) == 0:
        return 0
    return sum([int(i) for i in str(max(lst))])


