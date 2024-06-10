operations_to_remainder(n, x, y, number):
    operations = 0
    for i in range(n - 1, n - 1 - x, -1):
        if i == n - 1 - y:
            if number[i] == '0':
                operations += 1
        else:
            if number[i] == '1':
                operations += 1
    return operations

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    number = input().strip()
    print(min_operations_to_remainder(n, x, y, number))
