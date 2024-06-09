
def plus_one(digits):
    
    digits[-1] += 1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        else:
            break
    return digits

