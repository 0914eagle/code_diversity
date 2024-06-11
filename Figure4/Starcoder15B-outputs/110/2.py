def exchange(lst1, lst2):
    
    lst1_even = [x for x in lst1 if x % 2 == 0]
    lst2_even = [x for x in lst2 if x % 2 == 0]
    if len(lst1_even) == len(lst1) and len(lst2_even) == len(lst2):
        return "YES"
    else:
        return "NO"


