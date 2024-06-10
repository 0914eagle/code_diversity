
def get_digit_array(digits):
    
    if len(digits) == 0:
        return []
    else:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] > 9:
                digits[i] = 0
                if i != 0:
                    digits[i-1] += 1
        return digits

def plus_one(digits):
    
    if len(digits) == 0:
        return []
    else:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] > 9:
                digits[i] = 0
                if i != 0:
                    digits[i-1] += 1
        return digits

if __name__ == '__main__':
    digits = [1, 2, 3]
    print(plus_one(digits))

