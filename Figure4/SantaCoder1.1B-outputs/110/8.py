def exchange(lst1, lst2):
    
    # Your code here
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0 and lst2[i] % 2 == 1:
            return "YES"
    return "NO"

