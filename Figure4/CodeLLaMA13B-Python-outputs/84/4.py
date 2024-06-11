def solve(N):
    
    # your code here
    binary = bin(N)[2:]
    sum = 0
    for i in binary:
        sum += int(i)
    return bin(sum)[2:]

if __name__ == '__main__':
   