
def get_longest_increasing_sequence(a):
    # Initialize variables
    n = len(a)
    left = [0] * n
    right = [0] * n
    longest = 0
    length = 0
    prev = -1

    # Compute the length of the longest increasing sequence
    for i in range(n):
        if a[i] > prev:
            length += 1
        else:
            length = 1
        prev = a[i]
        longest = max(longest, length)
        left[i] = length

    # Reset variables
    length = 0
    prev = 2 * 10**5 + 1

    # Compute the length of the longest increasing sequence from the right
    for i in range(n-1, -1, -1):
        if a[i] < prev:
            length += 1
        else:
            length = 1
        prev = a[i]
        right[i] = length

    # Find the maximum length and its corresponding string
    max_length = 0
    string = ""
    for i in range(n):
        length = left[i] + right[i] - 1
        if length > max_length:
            max_length = length
            string = "L" * left[i] + "R" * right[i]

    return max_length, string

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_length, string = get_longest_increasing_sequence(a)
    print(max_length)
    print(string)

if __name__ == '__main__':
    main()

