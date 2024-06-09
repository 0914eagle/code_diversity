
def get_maximum_candies(n, k):
    min_candies, max_candies = divmod(n, k)
    if max_candies == 0:
        return n
    if max_candies == 1:
        return n - 1
    floor_k_over_2 = k // 2
    for i in range(min_candies, max_candies):
        if max_candies - i <= floor_k_over_2:
            return n - i
    return n - min_candies

