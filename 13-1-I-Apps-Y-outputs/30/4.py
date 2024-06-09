
def get_min_divisible_by_2_and_n(n):
    # Find the smallest number that is divisible by both 2 and N
    return (n * 2) if (n * 2) % n == 0 else (n * 2) + 1

