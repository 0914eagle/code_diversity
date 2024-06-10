
def get_maximum_number(v, a):
    # Initialize variables
    max_number = 0
    current_digit = 1
    remaining_paint = v

    # Iterate through the digits of the maximum number
    while remaining_paint >= a[current_digit] and current_digit <= 9:
        # Calculate the current digit of the maximum number
        current_digit_value = int(remaining_paint / a[current_digit])
        max_number = max_number * 10 + current_digit_value
        remaining_paint = remaining_paint % a[current_digit]
        current_digit += 1

    # Check if the maximum number has any zeroes
    if "0" in str(max_number):
        return -1

    return max_number

def main():
    v = int(input())
    a = list(map(int, input().split()))
    print(get_maximum_number(v, a))

if __name__ == '__main__':
    main()

