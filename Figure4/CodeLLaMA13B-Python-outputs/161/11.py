def solve(s):
    
    # your code here
    if s.isalpha():
        return s.swapcase()
    else:
        return s[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
