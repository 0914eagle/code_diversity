
def get_arithmetic_progression(n, a):
    # Calculate the common difference of the arithmetic progression
    common_diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != common_diff:
            return -1
    return common_diff

def get_missing_number(n, a):
    # Calculate the common difference of the arithmetic progression
    common_diff = get_arithmetic_progression(n, a)
    if common_diff == -1:
        return -1
    # Calculate the missing number
    missing_number = a[0] + common_diff * (n-1)
    return missing_number

def get_all_numbers(n, a):
    # Calculate the common difference of the arithmetic progression
    common_diff = get_arithmetic_progression(n, a)
    if common_diff == -1:
        return -1
    # Calculate all the numbers in the arithmetic progression
    all_numbers = [a[0] + common_diff * i for i in range(n)]
    return all_numbers

def main():
    n = int(input())
    a = list(map(int, input().split()))
    missing_number = get_missing_number(n, a)
    if missing_number == -1:
        print(-1)
    else:
        all_numbers = get_all_numbers(n, a)
        print(len(all_numbers))
        print(*all_numbers)

if __name__ == '__main__':
    main()

