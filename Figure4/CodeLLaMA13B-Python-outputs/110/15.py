def exchange(lst1, lst2):
    
    # your code here
    even_lst = []
    odd_lst = []
    for i in lst1:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    if len(even_lst) == len(lst1):
        return "YES"
    else:
        for i in lst2:
            if i % 2 == 0:
                even_lst.append(i)
            else:
                odd_lst.append(i)
        if len(even_lst) == len(lst1) + len(lst2):
            return "YES"
        else:
            return "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
