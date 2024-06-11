def exchange(lst1, lst2):
    
    # Your code here
    # lst1 = [1, 2, 3, 4]
    # lst2 = [1, 5, 3, 4]
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0 and lst2[i] % 2 != 0:
            return "NO"
    return "YES"


