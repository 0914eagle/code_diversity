def sum_squares(lst):
    
    # Solution 1
    # lst_copy = lst.copy()
    # for i in range(len(lst)):
    #     if i % 3 == 0:
    #         lst_copy[i] = lst[i]**2
    #     elif i % 4 == 0 and i % 3 != 0:
    #         lst_copy[i] = lst[i]**3
    # return sum(lst_copy)
    
    # Solution 2
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)))
    
    # Solution 3
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 4
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 5
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 6
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 7
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 8
    # return sum(lst[i]**(2 if i % 3 == 0 else 3) for i in range(len(lst)) if i % 3 == 0 or i % 4 == 0)
    
    # Solution 9
