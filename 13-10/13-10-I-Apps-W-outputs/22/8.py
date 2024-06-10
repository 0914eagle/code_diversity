
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def count_sorted_pairs(arr, x):
    count = 0
    for l in range(1, x + 1):
        for r in range(l, x + 1):
            temp = arr[:]
            temp = [i for i in temp if l <= i <= r]
            if is_sorted(temp):
                count += 1
    return count

def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_sorted_pairs(arr, x))

if __name__ == '__main__':
    main()

