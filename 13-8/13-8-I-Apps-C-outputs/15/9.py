
import itertools

def is_sorted(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                return False
    return True

def count_unsorted_sequences(arr):
    count = 0
    for perm in itertools.permutations(arr):
        if not is_sorted(perm):
            count += 1
    return count % (10**9 + 9)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_unsorted_sequences(arr))

if __name__ == '__main__':
    main()

