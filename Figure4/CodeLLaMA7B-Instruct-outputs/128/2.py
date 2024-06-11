

def prod_signs(arr):
    
    if not arr:
        return None

    product = 1
    sum_of_magnitudes = 0

    for num in arr:
        if num == 0:
            product = 0
        else:
            product *= num // abs(num)
        sum_of_magnitudes += abs(num)

    return sum_of_magnitudes * product


