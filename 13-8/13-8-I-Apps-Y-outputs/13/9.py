
def plus_one(digits):
    
    # Add 1 to the last digit
    digits[-1] += 1

    # If the last digit is greater than 9, we need to carry the 1 to the next digit
    if digits[-1] == 10:
        digits[-1] = 0
        if len(digits) > 1:
            plus_one(digits[:-1])
        else:
            digits.append(1)

    return digits

def main():
    digits = [1, 2, 3]
    print(plus_one(digits))  # output: [1, 2, 4]

    digits = [4, 3, 2, 1]
    print(plus_one(digits))  # output: [4, 3, 2, 2]

if __name__ == '__main__':
    main()

