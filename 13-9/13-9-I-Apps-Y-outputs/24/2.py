
def get_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr

def find_max_diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    n, arr = get_input()
    print(find_max_diff(arr))

if __name__ == '__main__':
    main()

