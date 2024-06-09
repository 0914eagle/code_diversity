
def get_pairs(n, arr):
    pairs = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] & arr[j] >= arr[i] ^ arr[j]:
                pairs += 1
    return pairs

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_pairs(n, arr))

if __name__ == '__main__':
    main()

