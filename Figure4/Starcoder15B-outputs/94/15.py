def skjkasdkd(lst):
    
    lst = [x for x in lst if x > 0]
    if len(lst) == 0:
        return 0
    lst = [x for x in lst if is_prime(x)]
    if len(lst) == 0:
        return 0
    return sum(list(map(int, str(max(lst)))))

