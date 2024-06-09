
def f1(n, k):
    result = n
    for i in range(k):
        if result % 10 != 0:
            result -= 1
        else:
            result //= 10
    return result

