
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    longest = 0
    longest_index = -1

    # Compute the length of the longest increasing sequence that ends at index i and starts at the left
    for i in range(n):
        if i == 0:
            left[i] = 1
        else:
            left[i] = max(left[i-1], 1)
        if a[i] > a[i-1]:
            left[i] += 1

    # Compute the length of the longest increasing sequence that ends at index i and starts at the right
    for i in range(n-1, -1, -1):
        if i == n-1:
            right[i] = 1
        else:
            right[i] = max(right[i+1], 1)
        if a[i] > a[i+1]:
            right[i] += 1

    # Find the index with the longest increasing sequence
    for i in range(n):
        if left[i] + right[i] - 1 > longest:
            longest = left[i] + right[i] - 1
            longest_index = i

    # Construct the sequence
    seq = []
    i = longest_index
    while i >= 0:
        if left[i] > right[i]:
            seq.append('L')
            i -= 1
        else:
            seq.append('R')
            i += 1

    return longest, ''.join(seq[::-1])

def main():
    n = int(input())
    a = list(map(int, input().split()))
    longest, seq = get_longest_increasing_sequence(a)
    print(longest)
    print(seq)

if __name__ == '__main__':
    main()

