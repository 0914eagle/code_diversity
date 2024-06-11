def rounded_avg(n, m):
    
    if n > m:
        return -1
    if n == m:
        return "0b" + str(n)
    else:
        return "0b" + str(n) + str(m)


