def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    if num < 0:
        num = -num
    while num > 0:
        if num % 10 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return even_count, odd_count


if __name__ == "__main__":
    print(even_odd_count(-12))
    print(even_odd_count(123))
