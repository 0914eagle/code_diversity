def sum_squares(lst):
    
    # Solution 1
    # lst_new = []
    # for i in range(len(lst)):
    #     if i % 3 == 0:
    #         lst_new.append(lst[i]**2)
    #     elif i % 4 == 0 and i % 3 != 0:
    #         lst_new.append(lst[i]**3)
    #     else:
    #         lst_new.append(lst[i])
    # return sum(lst_new)
    
    # Solution 2
    # lst_new = []
    # for i in range(len(lst)):
    #     if i % 3 == 0:
    #         lst_new.append(lst[i]**2)
    #     elif i % 4 == 0:
    #         lst_new.append(lst[i]**3)
    #     else:
    #         lst_new.append(lst[i])
    # return sum(lst_new)
    
    # Solution 3
    lst_new = []
    for i in range(len(lst)):
        if i % 3 == 0:
            lst_new.append(lst[i]**2)
        elif i % 4 == 0:
            lst_new.append(lst[i]**3)
        else:
            lst_new.append(lst[i])
    return sum(lst_new)

if __name__ == "__main__":
    print(sum_squares([1,2,3]))
    print(sum_squares([]))
    print(sum_squares([-1,-5,2,-1,-5]))
