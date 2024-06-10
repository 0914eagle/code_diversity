
def is_good(s):
    count_zeros = 0
    count_ones = 0
    for c in s:
        if c == '0':
            count_zeros += 1
        else:
            count_ones += 1
    return count_zeros != count_ones

def find_solution(s):
    if not is_good(s):
        return []
    if len(s) == 1:
        return [s]
    for i in range(1, len(s)):
        if is_good(s[:i]) and is_good(s[i:]):
            return [s[:i], s[i:]]
    return []

def main():
    n = int(input())
    s = input()
    solution = find_solution(s)
    print(len(solution))
    for s in solution:
        print(s, end=" ")

if __name__ == '__main__':
    main()

