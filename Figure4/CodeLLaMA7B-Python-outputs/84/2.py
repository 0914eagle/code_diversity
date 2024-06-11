def solve(N):
    
    # Your code here
    # convert N to binary
    # sum the digits
    # convert the sum to binary
    # return the binary string
    return bin(sum(int(x) for x in str(bin(N))[2:]))[2:]


if