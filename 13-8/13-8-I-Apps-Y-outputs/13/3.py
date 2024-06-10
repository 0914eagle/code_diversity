
def plus_one(digits):
    
    # Check if the last digit is 9
    if digits[-1] == 9:
        # If the last digit is 9, we need to plus one to the previous digit
        digits[-1] = 0
        return plus_one(digits[:-1]) + [1]
    else:
        # If the last digit is not 9, we just plus one to the last digit
        return digits[:-1] + [digits[-1] + 1]

def main():
    print(plus_one([1, 2, 3])) # output: [1, 2, 4]
    print(plus_one([4, 3, 2, 1])) # output: [4, 3, 2, 2]

if __name__ == '__main__':
    main()

