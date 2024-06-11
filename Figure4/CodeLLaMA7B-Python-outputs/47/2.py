def median(l: list):
    
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2] + l[n // 2 - 1]) / 2.0


if __name