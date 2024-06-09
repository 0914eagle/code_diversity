
def get_arithmetic_sequence(n, a):
    # Calculate the common difference of the sequence
    common_diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != common_diff:
            return -1
    # Calculate the first term of the sequence
    first_term = a[0]
    # Calculate the last term of the sequence
    last_term = a[n-1] + common_diff*(n-1)
    return [first_term, last_term]

def get_possible_numbers(n, a):
    # Get the arithmetic sequence
    seq = get_arithmetic_sequence(n, a)
    if seq == -1:
        return -1
    # Calculate the possible numbers
    possible_numbers = set()
    for i in range(seq[0], seq[1] + 1):
        if i not in a:
            possible_numbers.add(i)
    return possible_numbers

def main():
    n = int(input())
    a = list(map(int, input().split()))
    possible_numbers = get_possible_numbers(n, a)
    if possible_numbers == -1:
        print(-1)
    else:
        print(len(possible_numbers))
        print(*sorted(possible_numbers))

if __name__ == '__main__':
    main()

