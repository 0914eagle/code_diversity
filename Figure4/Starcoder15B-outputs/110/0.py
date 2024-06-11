def exchange(lst1, lst2):
    
    lst1_even = 0
    lst1_odd = 0
    lst2_even = 0
    lst2_odd = 0
    for i in lst1:
        if i % 2 == 0:
            lst1_even += 1
        else:
            lst1_odd += 1
    for i in lst2:
        if i % 2 == 0:
            lst2_even += 1
        else:
            lst2_odd += 1
    if lst1_even + lst2_odd == len(lst1) and lst1_odd + lst2_even == len(lst2):
        return "YES"
    else:
        return "NO"


