def rounded_avg(n, m):
    
    if n > m:
        return -1
    else:
        sum = 0
        for i in range(n, m+1):
            sum += i
        sum = sum / (m-n+1)
        sum = round(sum)
        return bin(sum)

print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))