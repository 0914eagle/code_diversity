def solve(N):
    
    # 1. Take input
    # 2. Convert to binary
    # 3. Add digits
    # 4. Return binary string
    return bin(N)[2:].replace('0', '1').replace('1', '0')


# 1. Take input
N = int(input())

# 2. Convert to binary
binary = solve(N)

# 3. Add digits
total = 0
for digit in binary:
    total += int(digit)

# 4. Return binary string
print(total)
