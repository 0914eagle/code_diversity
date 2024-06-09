
def get_maximum_candies(n, k):
    min_candies, max_candies = divmod(n, k)
    if max_candies == 0:
        return n
    for i in range(min_candies, max_candies):
        if n - i * (k // 2) >= 0:
            return n - i * (k // 2)
    return 0

