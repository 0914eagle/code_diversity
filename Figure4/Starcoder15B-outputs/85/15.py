def add(lst):
    
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum

