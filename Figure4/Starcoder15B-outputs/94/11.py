def skjkasdkd(lst):
    
    lst = [x for x in lst if x > 0]
    if not lst:
        return 0
    max_prime = max(lst)
    return sum(map(int, str(max_prime)))

