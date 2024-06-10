
def min_operations(n, x, y, number):
    operations = 0
    for i in range(n - x, n):
        if i == n - y - 1 and number[i] != '1':
            operations += 1
        elif i != n - y - 1 and number[i] != '0':
            operations += 1
    return operations

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    number = input().strip()
    print(min_operations(n, x, y, number))
