def prime_fib(n: int):
    
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

    # Fibonacci numbers are generated using matrix exponentiation
    # https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    # F_n = F_{n-1} * F_{n-2}
    # F_0 = 0, F_1 = 1
    # F_2 = F_0 * F_1 + F_1 * F_0 = 1
    # F_3 = F_1 * F_2 + F_2 * F_1 = 1 * 1 + 1 * 1 = 2
    # F_4 = F_2 * F_2 + F_3 * F_2 = 1 * 1 + 1 * 2 = 3
    # F_5 = F_3 * F_3 + F_4 * F_3 = 2 * 2 + 3 * 2 = 5
    # F_6 = F_4 * F_4 + F_5 * F_4 = 3 * 3 + 5 * 3 = 8
    # F_7 = F_5 * F_5 + F_6 * F_5 = 5 * 5 + 8 * 5 = 13
    # F_8 = F_6 * F_6 + F_7 * F_6 = 8 * 8 + 13 * 8 = 21
    # F_9 = F_7 * F_7 + F_8 * F_7 = 13 * 13 + 21 * 13 = 89

    # Matrix for Fibonacci sequence
    F = [[1, 1], [1, 0]]

    # Matrix for n-th Fibonacci number
    Fn = [[1, 1], [1, 0]]

    # Matrix for n-th Fibonacci number modulo n
    Fn