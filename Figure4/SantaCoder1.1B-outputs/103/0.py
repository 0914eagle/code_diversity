def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        return bin(n)[2:].zfill(m - n)

print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))
