
def is_good_array(arr):
    n = len(arr)
    if n % 6 != 0:
        return False
    seqs = [[] for _ in range(n//6)]
    for i in range(n):
        seqs[i//6].append(arr[i])
    for seq in seqs:
        if seq != [4, 8, 15, 16, 23, 42]:
            return False
    return True

def remove_elements(arr):
    n = len(arr)
    if n == 0:
        return 0
    if is_good_array(arr):
        return 0
    for i in range(n):
        arr_copy = arr[:i] + arr[i+1:]
        if is_good_array(arr_copy):
            return i
    return n

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_elements(arr))

