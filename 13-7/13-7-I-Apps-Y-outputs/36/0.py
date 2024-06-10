
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    longest = 0
    length = 0
    prev_left = -1
    prev_right = n

    # Loop through the array and find the longest increasing subsequence
    for i in range(n):
        left[i] = max(left[i-1], prev_left) if i > 0 else 0
        right[n-i-1] = min(right[n-i], prev_right) if i < n-1 else n-1
        length = max(length, right[i] - left[i] + 1)
        if length == n:
            break
        prev_left = left[i]
        prev_right = right[n-i-1]

    # Find the longest increasing subsequence
    seq = []
    i = 0
    while length > 0:
        if left[i] < prev_left:
            seq.append('L')
            prev_left = left[i]
        else:
            seq.append('R')
            prev_right = right[n-i-1]
        length -= 1
        i += 1

    return seq[::-1]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(get_longest_increasing_sequence(a)))
    print(''.join(get_longest_increasing_sequence(a)))

if __name__ == '__main__':
    main()

