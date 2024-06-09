
def get_min_steps(n, k):
    steps = 0
    while n > 0:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        steps += 1
    return steps

