
def get_longest_segment(arr):
    # find the longest segment of consecutive equal integers
    longest_segment = 1
    current_segment = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current_segment += 1
        else:
            longest_segment = max(longest_segment, current_segment)
            current_segment = 1
    longest_segment = max(longest_segment, current_segment)
    return longest_segment

def solve(arr):
    # find the number of operations needed to empty the array
    operations = 0
    while len(arr) > 0:
        longest_segment = get_longest_segment(arr)
        arr = arr[longest_segment:]
        operations += 1
    return operations

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

