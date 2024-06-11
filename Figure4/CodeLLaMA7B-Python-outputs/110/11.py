def exchange(lst1, lst2):
    
    # check if there are any odd numbers in lst1
    for num in lst1:
        if num % 2 == 1:
            return "NO"
    # check if there are any odd numbers in lst2
    for num in lst2:
        if num % 2 == 1:
            return "NO"
    # check if there are any odd numbers in lst1
    for num in lst1:
        if num % 2 == 1:
            return "NO"
    # check if there are any odd numbers in lst2
    for num in lst2:
        if num % 2 == 1:
            return "NO"
    return "YES"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
