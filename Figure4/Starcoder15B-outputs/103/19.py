def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        return bin(round(sum(range(n, m + 1)) / (m - n + 1)))

