

def add(lst):
    
    result = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            result += lst[i]
    return result

