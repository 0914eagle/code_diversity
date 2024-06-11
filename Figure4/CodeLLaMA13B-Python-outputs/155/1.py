def even_odd_count(num):
    
    if not isinstance(num, int):
        raise TypeError("num is not an integer.")
    even_count = 0
    odd_count = 0
    while num != 0:
        if num % 10 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return even_count, odd_count
