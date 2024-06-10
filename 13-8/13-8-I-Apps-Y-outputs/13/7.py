
def plus_one(digits):
    
    if len(digits) == 0:
        return []
    digits[-1] += 1
    i = len(digits) - 1
    while i > 0 and digits[i] == 10:
        digits[i] = 0
        i -= 1
        digits[i] += 1
    if digits[0] == 10:
        digits[0] = 0
        digits.insert(0, 1)
    return digits

def main():
    digits = [1, 2, 3]
    print(plus_one(digits))

if __name__ == '__main__':
    main()

