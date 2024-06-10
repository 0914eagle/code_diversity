operations(n, x, y, number):
    count = 0
    for i in range(n - x, n - y):
        if number[i] != '0':
            count += 1
    return count

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    number = input().strip()
    print(min_operations(n, x, y, number)