def sort_even(l: list):
    
    # Your code here
    l1 = []
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l2.sort()
    for i in range(len(l1)):
        l[i * 2] = l1[i]
    for i in range(len(l2)):
        l[i * 2 + 1] = l2[i]
    return l


print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
