
def get_min_changes(arr, k):
    n = len(arr)
    if n % k != 0:
        return -1
    
    count = 0
    for i in range(n // k):
        sub_arr = arr[i * k:(i + 1) * k]
        if sub_arr != arr[:k]:
            count += 1
    
    return count

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_min_changes(arr, k))

if __name__ == '__main__':
    main()

