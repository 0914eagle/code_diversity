def exchange(lst1, lst2):
    
    # Your code here
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0 and lst2[i] % 2 == 0:
            lst1[i] = lst1[i] + lst2[i]
            lst2[i] = lst1[i] - lst2[i]
            lst1[i] = lst1[i] - lst2[i]
            lst2[i] = lst1[i] + lst2[i]
        elif lst1[i] % 2 == 0 and lst2[i] % 2 != 0:
            return "NO"
        elif lst1[i] % 2 != 0 and lst2[i] % 2 == 0:
            return "NO"
    return "YES"

