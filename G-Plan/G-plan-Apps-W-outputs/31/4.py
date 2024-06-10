
def calculate_digit_sum(num):
    return sum(int(digit) for digit in str(num))

def find_max_digit_sum_integer(x):
    max_digit_sum = 0
    result = 0
    for num in range(x, 0, -1):
        digit_sum = calculate_digit_sum(num)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            result = num
    return result

if __name__ == "__main__":
    x = int(input())
    print(find_max_digit_sum_integer(x))
