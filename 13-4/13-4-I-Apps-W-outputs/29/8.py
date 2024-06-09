
def get_longest_segment(arr):
    if len(arr) == 0:
        return []
    
    longest = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            longest.append(arr[i])
        else:
            if len(longest) > len(arr[:i]):
                return longest
            longest = [arr[i]]
    
    if len(longest) > len(arr[:len(arr)]):
        return longest
    else:
        return arr

def solve(arr):
    count = 0
    while len(arr) > 0:
        count += 1
        arr = get_longest_segment(arr)
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

