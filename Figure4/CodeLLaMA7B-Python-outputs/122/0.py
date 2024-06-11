def add_elements(arr, k):
    
    # Time: O(n)
    # Space: O(1)
    if k == 0:
        return 0

    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) == 2:
            sum_two_digits += arr[i]

    return sum_two_digits + sum(arr[k:])


if __name__ == "__main__":
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    print(add