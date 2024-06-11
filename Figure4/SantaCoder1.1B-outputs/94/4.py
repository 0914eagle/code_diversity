def skjkasdkd(lst):
    
    # Your code here
    lst = sorted(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] * 10
    lst = [int(x) for x in str(sum(lst))]
    return lst[0]

