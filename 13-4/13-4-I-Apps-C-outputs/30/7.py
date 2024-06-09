
def get_median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]

def count_scary_subarrays(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] == get_median(arr[i:j+1]):
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_scary_subarrays(arr))

