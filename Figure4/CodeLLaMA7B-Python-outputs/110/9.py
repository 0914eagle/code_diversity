def exchange(lst1, lst2):
    
    # O(n) time, O(1) space
    if len(lst1) != len(lst2):
        return "NO"
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    if all(x % 2 == 0 for x in lst2):
        return "YES"
    if any(x % 2 == 0 for x in lst1) and any(x % 2 == 0 for x in lst2):
        return "NO"
    return "YES"

