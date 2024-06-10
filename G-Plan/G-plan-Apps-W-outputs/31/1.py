
def calculate_digit_sum(num):
    return sum(int(digit) for digit in str(num))

def find_max_digit_sum_integer(x):
    max_digit_sum = 0
    result = 0
    for i in range(x, 0, -1):
        digit_sum = calculate_digit_sum(i)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            result = i
    return result

if __name__ == "__main__":
    x = int(input())
    print(find_max_digit_sum_integer(x))
