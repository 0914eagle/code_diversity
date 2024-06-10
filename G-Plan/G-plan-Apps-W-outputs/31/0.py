
def calculate_digit_sum(num):
    return sum(map(int, str(num)))

def find_max_digit_sum_integer(x):
    max_sum = 0
    result = 0
    for num in range(x, 0, -1):
        if calculate_digit_sum(num) > max_sum:
            max_sum = calculate_digit_sum(num)
            result = num
    return result

if __name__ == "__main__":
    x = int(input())
    print(find_max_digit_sum_integer(x))
