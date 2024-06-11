def skjkasdkd(lst):
    
    lst = [i for i in lst if i > 0]
    if not lst:
        return 0
    lst = [i for i in lst if is_prime(i)]
    if not lst:
        return 0
    return sum(map(int, str(max(lst))))


