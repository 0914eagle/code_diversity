
def is_even(s):
    return s == s[::-1]

def longest_even(s):
    n = len(s)
    for i in range(n-1, 0, -1):
        if is_even(s[:i]):
            return i
    return 0

def main():
    s = input()
    print(longest_even(s))

if __name__ == '__main__':
    main()

