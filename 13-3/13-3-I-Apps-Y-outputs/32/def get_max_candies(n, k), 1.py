
def get_max_candies(n, k):
    min_candies = n // k
    max_candies = min_candies + 1
    count = 0
    for i in range(min_candies, max_candies+1):
        count = 0
        while n >= 0 and count < k:
            n -= i
            count += 1
        if count == k:
            return i
    return 0

