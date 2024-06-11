def rounded_avg(n, m):
    
    # Write your code here
    if n > m:
        return -1
    else:
        return bin(n)[2:].zfill(m - n + 1)

