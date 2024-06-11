def solve(s):
    
    # your code here
    if not s.isalpha():
        return s[::-1]
    else:
        return s.swapcase()


if __name__ == '__main__':
    f = open('input.txt', 'r')

    s = f.readline()
    s = s.strip()
    print(solve(s))
