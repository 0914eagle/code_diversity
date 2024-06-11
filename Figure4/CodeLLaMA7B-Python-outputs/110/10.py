def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"
    if len(lst1) != len(lst2):
        return "NO"
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    if all(x % 2 == 0 for x in lst2):
        return "YES"
    if all(x % 2 != 0 for x in lst1):
        return "NO"
    if all(x % 2 != 0 for x in lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0 and lst2[i] % 2 == 0:
            lst1[i], lst2[i] = lst2[i], lst1[i]
            if all(x % 2 == 0 for x in lst1):
                return "YES"
    return "NO"


