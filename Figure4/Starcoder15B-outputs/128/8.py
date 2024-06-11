def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    sum_ = 0
    for num in arr:
        if num == 0:
            sum_ += 0
        elif num < 0:
            prod *= -1
            sum_ += abs(num)
        else:
            sum_ += num
    return sum_ * prod


