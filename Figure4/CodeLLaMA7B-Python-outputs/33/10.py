def sort_third(l: list):
    
    l1 = []
    l2 = []
    l3 = []
    for i in l:
        if i % 3 == 0:
            l1.append(i)
        elif i % 3 == 1:
            l2.append(i)
        else:
            l3.append(i)
    l1.sort()
    l2.sort()
    l3.sort()
    return l1 + l2 + l3


print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
