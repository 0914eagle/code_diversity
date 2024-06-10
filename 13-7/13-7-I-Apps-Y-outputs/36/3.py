
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    length = 0
    max_length = 0
    max_length_index = 0
    s = ""

    # Compute the length of the longest increasing sequence
    for i in range(n):
        left[i] = 1 + left[i - 1] if i > 0 and a[i] > a[i - 1] else 1
        right[n - i - 1] = 1 + right[n - i] if i < n - 1 and a[n - i - 1] > a[n - i] else 1
        length = max(left[i], right[n - i - 1])
        if length > max_length:
            max_length = length
            max_length_index = i

    # Construct the longest increasing sequence
    i = max_length_index
    while i >= 0 and i < n:
        if left[i] == max_length:
            s += "L"
            i -= 1
        else:
            s += "R"
            i = n - i - 1

    return max_length, s[::-1]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(*get_longest_increasing_sequence(a))

if __name__ == '__main__':
    main()

