def exchange(lst1, lst2):
    
    even = 0
    odd = 0
    for i in lst1:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        return "YES"
    else:
        return "NO"


