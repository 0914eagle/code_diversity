def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"
    if len(lst1) != len(lst2):
        return "NO"
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    if all(x % 2 == 0 for x in lst2):
        return "YES"
    if any(x % 2 == 0 for x in lst1):
        return "NO"
    if any(x % 2 == 0 for x in lst2):
        return "NO"
    return "YES"


