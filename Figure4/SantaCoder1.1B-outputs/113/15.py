def odd_count(lst):
    
    odd_count = []
    for i in lst:
        odd_count.append(len(i) % 2)
    return odd_count


