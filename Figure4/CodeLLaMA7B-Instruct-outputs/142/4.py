



def sum_squares(lst):
    
    # Your code here
    result = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            result += x * x
        elif i % 4 == 0 and i % 3 != 0:
            result += x * x * x
    return result



