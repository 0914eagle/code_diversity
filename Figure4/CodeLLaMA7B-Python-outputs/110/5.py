def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"
    if len(lst1) != len(lst2):
        return "NO"
    lst1_even = [i for i in lst1 if i % 2 == 0]
    lst2_even = [i for i in lst2 if i % 2 == 0]
    lst1_odd = [i for i in lst1 if i % 2 != 0]
    lst2_odd = [i for i in lst2 if i % 2 != 0]
    if len(lst1_even) == len(lst2_even):
        return "YES"
    elif len(lst1_even) > len(lst2_even):
        return "NO"
    else:
        return "YES"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
