
def is_second_smallest(arr, i):
    if i == 0:
        return arr[i] < arr[i+1] and arr[i] < arr[i+2]
    elif i == len(arr) - 1:
        return arr[i-1] < arr[i] and arr[i] < arr[i+1]
    else:
        return arr[i-1] < arr[i] and arr[i] < arr[i+1] and arr[i] < arr[i+2]

def count_second_smallest(arr):
    count = 0
    for i in range(1, len(arr)-1):
        if is_second_smallest(arr, i):
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_second_smallest(arr))

