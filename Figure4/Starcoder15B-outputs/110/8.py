def exchange(lst1, lst2):
    
    lst1_even = []
    lst1_odd = []
    for i in lst1:
        if i % 2 == 0:
            lst1_even.append(i)
        else:
            lst1_odd.append(i)
    lst2_even = []
    lst2_odd = []
    for i in lst2:
        if i % 2 == 0:
            lst2_even.append(i)
        else:
            lst2_odd.append(i)
    if len(lst1_odd) <= len(lst2_even):
        return "YES"
    else:
        return "NO"


