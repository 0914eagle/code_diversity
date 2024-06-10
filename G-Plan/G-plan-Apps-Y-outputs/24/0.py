operations_to_remainder(n, x, y, number):
    count = 0
    for i in range(n - 1, n - 1 - x, -1):
        if i == n - 1 - y:
            count += 1 if number[i] == '0' else 0
        else:
            count += 1 if number[i] == '1' else 0
    return count

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    number = input().strip()
    print(min_operations_to_remainder(n, x, y, number)) 
