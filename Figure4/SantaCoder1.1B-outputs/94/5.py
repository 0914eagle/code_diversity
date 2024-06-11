def skjkasdkd(lst):
    
    lst = sorted(lst)
    max_prime = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_prime:
            max_prime = lst[i]
    return sum(map(int, str(max_prime)))


if __