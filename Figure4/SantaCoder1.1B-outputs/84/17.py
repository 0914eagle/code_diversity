def solve(N):
    
    # Your code here
    if N == 0:
        return "0"
    else:
        return str(bin(N)[2:])

if