def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"
    if len(lst1) != len(lst2):
        return "NO"
    if all(x % 2 == 0 for x in lst1) and all(x % 2 == 0 for x in lst2):
        return "YES"
    if all(x % 2 == 0 for x in lst1) and not all(x % 2 == 0 for x in lst2):
        return "NO"
    if all(x % 2 != 0 for x in lst1) and all(x % 2 == 0 for x in lst2):
        return "YES"
    if all(x % 2 != 0 for x in lst1) and not all(x % 2 == 0 for x in lst2):
        return "NO"
    if all(x % 2 == 0 for x in lst1) and all(x % 2 != 0 for x in lst2):
        return "YES"
    if all(x % 2 != 0 for x in lst1) and all(x % 2 != 0 for x in lst2):
        return "YES"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
