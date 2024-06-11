def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"

    if len(lst1) != len(lst2):
        return "NO"

    lst1_even = [num for num in lst1 if num % 2 == 0]
    lst2_even = [num for num in lst2 if num % 2 == 0]

    if len(lst1_even) != len(lst2_even):
        return "NO"

    return "YES"
