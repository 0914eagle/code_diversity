
def plus_one(digits):
    
    # check if the last digit is 9
    if digits[-1] != 9:
        # if not, just plus one to the last digit and return the result
        digits[-1] += 1
        return digits
    else:
        # if the last digit is 9, start from the end and check if the previous digit is 9
        for i in range(len(digits)-2, -1, -1):
            if digits[i] != 9:
                # if not, plus one to the previous digit and return the result
                digits[i] += 1
                return digits
        # if all the digits are 9s, create a new list and add a 1 to the beginning
        return [1] + digits

def main():
    digits = [1, 2, 3]
    result = plus_one(digits)
    print(result)

if __name__ == '__main__':
    main()

