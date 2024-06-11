def solve(s):
    
    # your code here
    if not s.isalpha():
        return s[::-1]
    else:
        return s.swapcase()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
