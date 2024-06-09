
def get_longest_segment(arr):
    longest = 1
    current = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

def get_number_of_operations(arr):
    longest = get_longest_segment(arr)
    return len(arr) // longest

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_number_of_operations(arr))

