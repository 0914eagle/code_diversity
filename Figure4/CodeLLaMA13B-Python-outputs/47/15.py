def median(l: list):
    
    l.sort()
    n = len(l)
    if n % 2 == 0:
        median1 = l[n // 2]
        median2 = l[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = l[n // 2]
    return median


