def add_elements(arr, k):
    
    if k == 0:
        return 0

    if k == 1:
        return sum(arr)

    if k == len(arr):
        return sum(arr)

    # 1. find the first digit
    first_digit = 0
    for i in range(k):
        first_digit = max(first_digit, len(str(arr[i])))

    # 2. find the second digit
    second_digit = 0
    for i in range(k):
        second_digit = max(second_digit, len(str(arr[i])))

    # 3. find the sum of the first digit
    first_digit_sum = 0
    for i in range(k):
        first_digit_sum += arr[i] // 10 ** (first_digit - 1)

    # 4. find the sum of the second digit
    second_digit_sum = 0
    for i in range(k):
        second_digit_sum += arr[i] % 10 ** second_digit

    return first_digit_sum + second_digit_sum


if __name__ == "__main__":
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    print(add_elements(arr, k))
