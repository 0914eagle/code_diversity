def solve(N):
    
    # 1. Take the input and convert it to binary
    # 2. Convert the binary number to a list of integers
    # 3. Sum the integers in the list
    # 4. Convert the sum to binary
    # 5. Return the binary number as a string
    return bin(int(N) + sum([int(i) for i in bin(N)[2:]]))[2:]


print(solve(147))
