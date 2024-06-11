def exchange(lst1, lst2):
    
    # Your code here
    # lst1 = [1, 2, 3, 4]
    # lst2 = [1, 5, 3, 4]
    # return "YES" if exchange(lst1, lst2) == "YES" else "NO"
    if len(lst1) != len(lst2):
        return "NO"
    if len(lst1) == 0:
        return "YES"
    if len(lst2) == 0:
        return "YES"
    if lst1[0] % 2 == 0 and lst2[0] % 2 == 0:
        return "YES"
    else:
        return "NO"


