def exchange(lst1, lst2):
    
    if not lst1 or not lst2:
        return "NO"

    if len(lst1) != len(lst2):
        return "NO"

    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i], lst2[i] = lst2[i], lst1[i]

    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            return "NO"

    return "YES"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
