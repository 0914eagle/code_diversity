
import sys

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(1, 1 << n):
        bits = bin(i)[2:]
        bits.zfill(n)
        sorted_seq = True
        for j in range(n):
            if bits[j] == '1':
                if arr[j] > arr[j+1]:
                    sorted_seq = False
                    break
        if sorted_seq:
            count += 1
    return count % (10**9 + 9)

n = int(input())
arr = list(map(int, input().split()))
print(get_entirely_unsorted_sequences(arr))

