def solve(N):
    
    # 1. Take the input and convert it to binary
    # 2. Add the binary digits together
    # 3. Convert the sum back to a binary number
    # 4. Return the binary number as a string
    return bin(sum(int(x) for x in str(bin(N))[2:]))[2:]


print(solve(1000))
print(solve(150))
print(solve(147))
