def exchange(lst1, lst2):
    
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst1_odd = [i for i in lst1 if i % 2 != 0]
    lst2_even = [i for i in lst2 if i % 2 == 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]
    if len(lst1_even) == len(lst1):
        return "YES"
    elif len(lst1_even) == 0:
        return "NO"
    else:
        if len(lst1_odd) <= len(lst2_even):
            return "YES"
        else:
            return "NO"


