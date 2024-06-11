def even_odd_count(num):
    
    if not isinstance(num, int):
        raise TypeError("Only integers are allowed")
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


if __