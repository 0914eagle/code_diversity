def odd_count(lst):
    
    odd_count = []
    for i in lst:
        odd_count.append(len([x for x in i if x.isdigit() and int(x)%2 != 0]))
    return odd_count

