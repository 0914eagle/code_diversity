
def get_accommodation_fee(n, k, x, y):
    total_fee = 0
    for i in range(1, n+1):
        if i <= k:
            total_fee += x
        else:
            total_fee += y
    return total_fee

