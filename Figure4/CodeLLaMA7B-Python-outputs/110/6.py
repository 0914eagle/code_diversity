def exchange(lst1, lst2):
    
    if lst1 == lst2:
        return "YES"
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i], lst2[i] = lst2[i], lst1[i]
            if lst1 == lst2:
                return "YES"
    return "NO"


