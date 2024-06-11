

def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        sum = (n + m) // 2
        return bin(sum)[2:]


