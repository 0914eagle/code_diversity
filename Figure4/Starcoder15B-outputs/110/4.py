def exchange(lst1, lst2):
    
    lst1_even = [x for x in lst1 if x % 2 == 0]
    lst1_odd = [x for x in lst1 if x % 2 != 0]
    lst2_even = [x for x in lst2 if x % 2 == 0]
    lst2_odd = [x for x in lst2 if x % 2 != 0]
    if len(lst1_even) == len(lst1):
        return "YES"
    elif len(lst1_even) == 0:
        return "NO"
    else:
        if len(lst1_even) > len(lst2_odd):
            return "NO"
        else:
            return "YES"


