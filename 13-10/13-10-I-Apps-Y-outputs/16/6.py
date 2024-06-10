
def get_good_array(arr):
    n = len(arr)
    if n % 6 != 0:
        return -1
    count = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        count[arr[i] - 4] += 1
    for i in range(6):
        if count[i] == 0:
            return -1
    return n - sum(count)

def get_min_removal(arr):
    n = len(arr)
    if n == 0:
        return 0
    min_removal = n
    for i in range(n):
        copy = arr[:]
        copy.pop(i)
        removal = get_min_removal(copy)
        if removal >= 0:
            min_removal = min(min_removal, removal + 1)
    return min_removal

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(get_min_removal(arr))

