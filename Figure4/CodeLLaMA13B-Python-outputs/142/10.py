def sum_squares(lst):
    
    # Solution 1
    # return sum([pow(x,3) if i%4==0 and i%3==0 else pow(x,2) if i%3==0 else x for i,x in enumerate(lst)])
    
    # Solution 2
    # return sum(map(lambda x: pow(x,3) if i%4==0 and i%3==0 else pow(x,2) if i%3==0 else x, lst))
    
    # Solution 3
    # return sum(map(lambda x: pow(x,3) if i%4==0 and i%3==0 else pow(x,2) if i%3==0 else x, enumerate(lst)))
    
    # Solution 4
    # return sum(map(lambda x: pow(x,3) if x[0]%4==0 and x[0]%3==0 else pow(x[1],2) if x[0]%3==0 else x[1], enumerate(lst)))
    
    # Solution 5
    # return sum(map(lambda x: pow(x,3) if x[0]%4==0 and x[0]%3==0 else pow(x[1],2) if x[0]%3==0 else x[1], enumerate(lst)))
    
    # Solution 6
    # return sum(map(lambda x: pow(x,3) if x[0]%4==0 and x[0]%3==0 else pow(x[1],2) if x[0]%3==0 else x[1], enumerate(lst)))
    
    # Solution 7
    # return sum(map(lambda x: pow(x,3) if x[0]%4==0 and x[0]%3==0 else pow(x[1],2) if x[0]%3==0 else x[1], enumerate(lst)))
    
    # Solution 8
    # return sum(map(lambda x: pow(x,3) if x[0]%4==0 and x[0]%3==0 else pow(x[1],2) if x[0]%3==0 else x[1