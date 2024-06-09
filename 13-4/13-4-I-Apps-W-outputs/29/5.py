
def get_longest_segment(arr):
    longest = 0
    current = 0
    for i in range(len(arr)):
        if arr[i] == arr[i-1] + 1:
            current += 1
        else:
            current = 0
        longest = max(longest, current)
    return longest

def solve(arr):
    count = 0
    while len(arr) > 0:
        count += 1
        longest = get_longest_segment(arr)
        arr = arr[longest:]
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

