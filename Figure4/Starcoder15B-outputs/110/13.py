def exchange(lst1, lst2):
    
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst1_odd = [i for i in lst1 if i % 2 != 0]
    lst2_even = [i for i in lst2 if i % 2 == 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]
    if len(lst1_even) > len(lst2_odd):
        return "NO"
    elif len(lst1_odd) > len(lst2_even):
        return "NO"
    else:
        return "YES"


