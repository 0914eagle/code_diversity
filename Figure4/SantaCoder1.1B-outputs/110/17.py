def exchange(lst1, lst2):
    
    # Your code here
    if len(lst1) != len(lst2):
        return "NO"
    if len(lst1) == 0:
        return "NO"
    if len(lst1) == 1:
        return "YES"
    if len(lst1) == 2:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0:
            return "YES"
        else:
            return "NO"
    if len(lst1) == 3:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0 and lst1[2] % 2 == 0:
            return "YES"
        else:
            return "NO"
    if len(lst1) == 4:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0 and lst1[2] % 2 == 0 and lst1[3] % 2 == 0:
            return "YES"
        else:
            return "NO"
    if len(lst1) == 5:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0 and lst1[2] % 2 == 0 and lst1[3] % 2 == 0 and lst1[4] % 2 == 0:
            return "YES"
        else:
            return "NO"
    if len(lst1) == 6:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0 and lst1[2] % 2 == 0 and lst1[3] % 2 == 0 and lst1[4] % 2 == 0 and lst1[5] % 2 == 0:
            return "YES"
        else:
            return "NO"
    if len(lst1) == 7:
        if lst1[0] % 2 == 0 and lst1[1] % 2 == 0 and lst1[2] % 2 == 0 and lst1[3] % 2 == 0 and lst1[4] % 2 == 0 and lst1[5] % 2 == 0 and lst1