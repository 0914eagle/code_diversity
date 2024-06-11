def solve(N):
    
    # your code here
    binary = bin(N)[2:]
    total = 0
    for i in binary:
        total += int(i)
    return bin(total)[2:]


if __name__ == '__