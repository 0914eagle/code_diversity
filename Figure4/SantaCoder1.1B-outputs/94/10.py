def skjkasdkd(lst):
    
    # Your code here
    lst = sorted(lst)
    max_prime = 0
    for i in range(len(lst)):
        if lst[i] > max_prime:
            max_prime = lst[i]
    return sum(str(max_prime))

