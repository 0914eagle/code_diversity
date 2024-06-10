
def find_longest_non_decreasing_sequence(n, T, arr):
    max_length = 1
    current_length = 1

    for i in range(1, n * T):
        if arr[i] >= arr[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)

if __name__ == '__main__':
    n, T = map(int, input().split())
    arr = list(map(int, input().split()))
    print(find_longest_non_decreasing_sequence(n, T, arr))
