def exchange(lst1, lst2):
    
    # Your code here
    even_lst1 = [i for i in lst1 if i % 2 == 0]
    odd_lst1 = [i for i in lst1 if i % 2 != 0]
    even_lst2 = [i for i in lst2 if i % 2 == 0]
    odd_lst2 = [i for i in lst2 if i % 2 != 0]
    if len(even_lst1) == len(lst1):
        return "YES"
    elif len(even_lst1) + len(odd_lst2) == len(lst1):
        return "YES"
    elif len(even_lst1) + len(even_lst2) == len(lst1):
        return "YES"
    else:
        return "NO"


