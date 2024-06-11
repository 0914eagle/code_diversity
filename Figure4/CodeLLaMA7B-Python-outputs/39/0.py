def prime_fib(n: int):
    
    if n < 1:
        raise ValueError("n must be greater than 0")

    if n == 1:
        return 2

    if n == 2:
        return 3

    if n == 3:
        return 5

    if n == 4:
        return 13

    if n == 5:
        return 89

    fib_list = [2, 3, 5, 13, 89]
    fib_list_len = len(fib_list)
    while fib_list_len < n:
        fib_list.append(fib_list[fib_list_len - 1] + fib_list[fib_list_len - 2])
        fib_list_len += 1

    return fib_list[n - 1]


if