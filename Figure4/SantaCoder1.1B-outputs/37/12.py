def sort_even(l: list):
    
    l.sort()
    even = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
    return even


