
def is_good_array(arr):
    if len(arr) % 6 != 0:
        return False
    subseq_count = 0
    for i in range(0, len(arr), 6):
        subseq = arr[i:i+6]
        if subseq != [4, 8, 15, 16, 23, 42]:
            return False
        subseq_count += 1
    return subseq_count == len(arr) // 6

def remove_elements_to_make_good(arr):
    removed_elements = 0
    while not is_good_array(arr):
        removed_elements += 1
        arr.pop()
    return removed_elements

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_elements_to_make_good(arr))

if __name__ == '__main__':
    main()

