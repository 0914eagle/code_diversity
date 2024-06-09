
def get_longest_segment(arr):
    # find the longest segment of consecutive equal integers
    longest = 1
    current = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return longest

def remove_segment(arr, segment):
    # remove the longest segment from the array
    return arr[segment:]

def count_operations(arr):
    # count the number of operations needed to remove all elements from the array
    operations = 0
    while len(arr) > 0:
        segment = get_longest_segment(arr)
        arr = remove_segment(arr, segment)
        operations += 1
    return operations

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_operations(arr))

