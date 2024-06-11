def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        return bin(int(round((m+n)/2)))[2:]


if