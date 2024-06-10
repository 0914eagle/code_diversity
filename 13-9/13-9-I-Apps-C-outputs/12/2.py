
def get_max_sum(arr):
    n = len(arr) // 2
    arr.sort()
    return sum(arr[:n]) + sum(arr[n:])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_sum(arr))

if __name__ == '__main__':
    main()

