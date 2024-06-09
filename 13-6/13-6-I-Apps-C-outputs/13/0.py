
def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_entirely_unsorted_sequences(arr) % (10**9 + 9))

if __name__ == '__main__':
    main()

