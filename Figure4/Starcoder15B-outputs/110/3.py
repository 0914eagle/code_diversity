def exchange(lst1, lst2):
    
    lst1_even = 0
    lst2_odd = 0
    for i in lst1:
        if i % 2 == 0:
            lst1_even += 1
    for i in lst2:
        if i % 2 != 0:
            lst2_odd += 1
    if lst1_even == len(lst1) or lst2_odd == len(lst2):
        return "YES"
    else:
        return "NO"


