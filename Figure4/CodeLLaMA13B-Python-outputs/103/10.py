def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        sum = 0
        for i in range(n, m+1):
            sum += i
        return bin(round(sum/(m-n+1)))


