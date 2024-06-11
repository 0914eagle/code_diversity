def rounded_avg(n, m):
    
    if n > m:
        return -1
    return bin(round((n + m) / 2))

# print(rounded_avg(1, 5))
