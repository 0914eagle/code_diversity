
def read_input():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    return n, T, a

def longest_non_decreasing_sequence(a):
    max_length = 1
    current_length = 1
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length

def solve(n, T, a):
    longest = 0
    for i in range(n, len(a)):
        longest = max(longest, longest_non_decreasing_sequence(a[i-n:i]))
    return longest

if __name__ == '__main__':
    n, T, a = read_input()
    print(solve(n, T, a))

