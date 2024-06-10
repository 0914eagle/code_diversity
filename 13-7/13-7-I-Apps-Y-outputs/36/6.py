
def get_longest_increasing_sequence(a):
    n = len(a)
    if n == 1:
        return 1, "R"
    left = [0] * n
    right = [0] * n
    left[0] = 1
    right[n-1] = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            left[i] = left[i-1] + 1
        else:
            left[i] = 1
    for i in range(n-2, -1, -1):
        if a[i] > a[i+1]:
            right[i] = right[i+1] + 1
        else:
            right[i] = 1
    max_len = 0
    longest_seq = ""
    for i in range(n):
        curr_len = left[i] + right[i] - 1
        if curr_len > max_len:
            max_len = curr_len
            longest_seq = "L" * left[i] + "R" * right[i]
    return max_len, longest_seq

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_longest_increasing_sequence(a))

if __name__ == '__main__':
    main()

