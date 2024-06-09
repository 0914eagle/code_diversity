
def get_pattern_length(pattern):
    return len(pattern.replace("*", ""))

def get_max_members(n, pattern):
    pattern_length = get_pattern_length(pattern)
    if pattern_length == n:
        return 2**n
    else:
        return 2**(n-pattern_length)

def main():
    n = int(input())
    pattern = input()
    print(get_max_members(n, pattern))

if __name__ == '__main__':
    main()

