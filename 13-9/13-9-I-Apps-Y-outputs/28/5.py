
def is_second_smallest(arr, i):
    if i == 0:
        return arr[i] < arr[i + 1] and arr[i] < arr[i + 2]
    if i == len(arr) - 1:
        return arr[i - 1] < arr[i] and arr[i] < arr[i - 1]
    return arr[i - 1] < arr[i] and arr[i] < arr[i + 1]

def count_second_smallest(arr):
    count = 0
    for i in range(1, len(arr) - 1):
        if is_second_smallest(arr, i):
            count += 1
    return count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_second_smallest(arr))

if __name__ == '__main__':
    main()

