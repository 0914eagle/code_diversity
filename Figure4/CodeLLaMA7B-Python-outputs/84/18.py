def solve(N):
    
    # 1. Take the input and convert it to binary
    # 2. Split the binary number into digits
    # 3. Sum the digits
    # 4. Convert the sum to binary
    # 5. Return the binary number
    return bin(sum([int(x) for x in str(bin(N))[2:]])).replace("0b", "")


if __name__ == '__main__':
    print(solve(1000))
