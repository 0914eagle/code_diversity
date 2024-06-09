
def get_max_sum(k2, k3, k5, k6):
    digits = [2] * k2 + [3] * k3 + [5] * k5 + [6] * k6
    digits.sort(reverse=True)
    sum = 0
    for i in range(len(digits)):
        if digits[i] == 2:
            sum += 256
            digits[i] = 0
        elif digits[i] == 3:
            sum += 32
            digits[i] = 0
        else:
            break
    return sum

