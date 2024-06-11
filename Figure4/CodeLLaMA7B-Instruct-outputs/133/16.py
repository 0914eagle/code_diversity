


def sum_squares(lst):
    
    # raise NotImplementedError()
    # Your code here
    lst = [int(round(x)) for x in lst]
    return sum([x**2 for x in lst])

