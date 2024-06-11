def rounded_avg(n, m):
    
    if n > m:
        return -1
    return bin(round((m+n)/2))[2:]


if __name