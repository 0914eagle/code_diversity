def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        avg = (n + m) / 2
        return bin(int(avg))


print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))
