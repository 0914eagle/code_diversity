
def get_xor_pairs(arr):
    n = len(arr)
    xor_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            xor = arr[i] ^ arr[j]
            if xor == sum(arr[i:j+1]):
                xor_pairs += 1
    return xor_pairs

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_xor_pairs(arr))

if __name__ == '__main__':
    main()

