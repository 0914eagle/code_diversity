def solve(N):
    
    # 1. Take input
    # 2. Convert to binary
    # 3. Sum the digits
    # 4. Convert to binary
    # 5. Return the sum
    return bin(sum(int(i) for i in str(bin(N))[2:]))[2:]


if __name__ == '__main__':
    print(solve(1000))
    print(solve(150))
    print(solve(147))
