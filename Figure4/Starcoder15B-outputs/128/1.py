def prod_signs(arr):
    
    if not arr:
        return None
    prod = 1
    sum_ = 0
    for i in arr:
        if i == 0:
            sum_ += 0
        elif i > 0:
            sum_ += 1
        else:
            sum_ -= 1
        prod *= i
    return sum_ * prod


if