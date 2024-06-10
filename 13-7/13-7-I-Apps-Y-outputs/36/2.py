
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    longest = 0
    longest_index = -1

    # Compute the length of the longest increasing subsequence from the left
    for i in range(n):
        left[i] = 1
        for j in range(i):
            if a[i] > a[j] and left[i] < left[j] + 1:
                left[i] = left[j] + 1
        if left[i] > longest:
            longest = left[i]
            longest_index = i

    # Compute the length of the longest increasing subsequence from the right
    for i in range(n-1, -1, -1):
        right[i] = 1
        for j in range(i+1, n):
            if a[i] > a[j] and right[i] < right[j] + 1:
                right[i] = right[j] + 1
        if right[i] > longest:
            longest = right[i]
            longest_index = i

    # Construct the longest increasing subsequence
    seq = []
    i = longest_index
    while i != -1:
        seq.append(a[i])
        i = left[i] if i > 0 else -1
    seq.reverse()

    # Return the length of the longest increasing subsequence and the sequence
    return (longest, "".join("L" if a[i] > a[i-1] else "R" for i in range(1, len(seq))))

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_longest_increasing_sequence(a))

if __name__ == '__main__':
    main()

