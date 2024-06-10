
def read_input():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    return n, m, arr

def lossy_sort(arr, m):
    # Sort the array
    arr.sort()
    # Find the minimum number of digits to change
    min_digits = m - 1
    for i in range(n - 1):
        for j in range(m):
            if arr[i][j] != arr[i + 1][j]:
                min_digits = min(min_digits, j)
                break
    # Make the minimum number of digit changes
    for i in range(n - 1):
        for j in range(min_digits):
            if arr[i][j] > arr[i + 1][j]:
                arr[i][j] -= 1
            elif arr[i][j] < arr[i + 1][j]:
                arr[i][j] += 1
    return arr

def main():
    n, m, arr = read_input()
    sorted_arr = lossy_sort(arr, m)
    for num in sorted_arr:
        print(num)

if __name__ == '__main__':
    main()

