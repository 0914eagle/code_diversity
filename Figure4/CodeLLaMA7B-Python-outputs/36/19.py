def fizz_buzz(n: int):
    
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).find("7") != -1:
                count += 1
    return count


if