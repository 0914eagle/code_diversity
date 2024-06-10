
def plus_one(digits):
    
    # Check if the last digit is 9
    if digits[-1] != 9:
        # If not, increment the last digit and return the result
        digits[-1] += 1
        return digits
    else:
        # If the last digit is 9, start from the end and increment the next digit that is not 9
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
        # If all digits are 9, create a new array with a single digit 1 and return it
        return [1]

def main():
    print(plus_one([1, 2, 3]))
    print(plus_one([4, 3, 2, 1]))

if __name__ == "__main__":
    main()

