
def get_smallest_larger_number(x):
    # convert the input to a list of individual digits
    digits = [int(digit) for digit in str(x)]
    # sort the digits in ascending order
    sorted_digits = sorted(digits)
    # check if the digits are already in descending order
    if sorted_digits == digits:
        # if they are, return 0 as there is no smaller number
        return 0
    # if the digits are not already in descending order, find the smallest number larger than x
    largest_digit = max(digits)
    largest_digit_index = digits.index(largest_digit)
    # create a new list of digits with the largest digit removed
    new_digits = digits[:largest_digit_index] + digits[largest_digit_index+1:]
    # add the largest digit to the end of the list
    new_digits.append(largest_digit)
    # sort the digits in ascending order
    sorted_new_digits = sorted(new_digits)
    # return the smallest number larger than x
    return int("".join(map(str, sorted_new_digits)))

def main():
    x = int(input())
    print(get_smallest_larger_number(x))

if __name__ == '__main__':
    main()

