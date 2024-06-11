def solve(N):
    
    binary = bin(N)[2:]
    sum = 0
    for i in binary:
        sum += int(i)
    return str(sum)

if