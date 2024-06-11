def solve(s):
    
    # your code here
    # return "".join(c.lower() if c.isupper() else c.upper() for c in s)
    # return "".join(c.swapcase() for c in s)
    # return s.swapcase() if s.isalpha() else s[::-1]
    return s.swapcase() if s.isalpha() else s[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
