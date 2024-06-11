def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        return bin(n)[2:].zfill(m)

