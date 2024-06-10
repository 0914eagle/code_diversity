
def is_good(s):
    count_zero = 0
    count_one = 0
    for c in s:
        if c == "0":
            count_zero += 1
        else:
            count_one += 1
    return count_zero != count_one

def solve(s):
    if len(s) == 1:
        return 1, [s]
    
    # Try all possible ways to split the string into two substrings
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        if is_good(left) and is_good(right):
            k1, substrings1 = solve(left)
            k2, substrings2 = solve(right)
            return k1 + k2, substrings1 + substrings2
    
    # If no good way to split the string is found, return the original string
    return 1, [s]

def main():
    n = int(input())
    s = input()
    k, substrings = solve(s)
    print(k)
    print(" ".join(substrings))

if __name__ == '__main__':
    main()

