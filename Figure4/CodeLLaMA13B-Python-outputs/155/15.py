def even_odd_count(num):
    
    even = 0
    odd = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


if