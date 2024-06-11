def solve(N):
    
    # 1. Take the input and convert it to binary
    # 2. Split the binary number into a list of digits
    # 3. Convert each digit to an integer
    # 4. Sum the integers
    # 5. Convert the sum to binary
    # 6. Return the binary number
    return bin(sum(int(x) for x in str(bin(N)[2:]) if x != '0'))[2:]


if __name__ == '__main__':
    print(solve(int(input().strip())))
