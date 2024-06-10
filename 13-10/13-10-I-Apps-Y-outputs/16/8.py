
def is_good_array(arr):
    if len(arr) % 6 != 0:
        return False
    
    seq_count = len(arr) // 6
    seq_map = {4: 0, 8: 0, 15: 0, 16: 0, 23: 0, 42: 0}
    for i in range(seq_count):
        seq_map[arr[i]] += 1
        if seq_map[arr[i]] == 0:
            return False
    
    for i in range(seq_count, len(arr)):
        if arr[i] not in [4, 8, 15, 16, 23, 42]:
            return False
    
    return True

def get_min_removals(arr):
    removals = 0
    while not is_good_array(arr):
        removals += 1
        arr.pop()
    
    return removals

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_min_removals(arr))

if __name__ == '__main__':
    main()

