
def plus_one(digits):
    
    # Check if the last digit is 9
    if digits[-1] == 9:
        # If it is 9, replace it with 0 and add 1 to the next digit
        digits[-1] = 0
        return plus_one(digits)
    else:
        # If it is not 9, add 1 to the last digit
        digits[-1] += 1
        return digits

def main():
    digits = [1, 2, 3]
    print(plus_one(digits))  # Output: [1, 2, 4]

    digits = [4, 3, 2, 1]
    print(plus_one(digits))  # Output: [4, 3, 2, 2]

if __name__ == '__main__':
    main()

