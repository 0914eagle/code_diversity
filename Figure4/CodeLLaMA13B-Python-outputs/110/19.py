def exchange(lst1, lst2):
    
    # your code here
    even_lst1 = []
    odd_lst1 = []
    even_lst2 = []
    odd_lst2 = []

    for i in lst1:
        if i % 2 == 0:
            even_lst1.append(i)
        else:
            odd_lst1.append(i)

    for i in lst2:
        if i % 2 == 0:
            even_lst2.append(i)
        else:
            odd_lst2.append(i)

    if len(odd_lst1) == len(even_lst2):
        return "YES"
    else:
        return "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
