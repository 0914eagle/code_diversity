def sum_squares(lst):
    
    
    # Solution
    return sum([pow(i, 3) if (idx+1) % 4 == 0 and (idx+1) % 3 != 0 else pow(i, 2) if (idx+1) % 3 == 0 else i for idx, i in enumerate(lst)])
    
    
    # Loop
    # result = 0
    # for idx, i in enumerate(lst):
    #     if (idx+1) % 3 == 0:
    #         result += pow(i, 2)
    #     elif (idx+1) % 4 == 0 and (idx+1) % 3 != 0:
    #         result += pow(i, 3)
    #     else:
    #         result += i
    # return result
    
    
    # List Comprehension
    # return sum([pow(i, 3) if (idx+1) % 4 == 0 and (idx+1) % 3 != 0 else pow(i, 2) if (idx+1) % 3 == 0 else i for idx, i in enumerate(lst)])
    
    
    # Map
    # return sum(map(lambda x: pow(x, 3) if (idx+1) % 4 == 0 and (idx+1) % 3 != 0 else pow(x, 2) if (idx+1) % 3 == 0 else x, lst))
    
    
    # Lambda
    # return sum(list(map(lambda x: pow(x, 3) if (idx+1) % 4 == 0 and (idx+1) % 3 != 0 else pow(x, 2) if (idx+1) % 3 == 0 else x, lst)))
