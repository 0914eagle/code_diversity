def solve(N):
    
    return bin(N)[2:].replace('0', '1').replace('1', '0')


if __name__ == '__main__':
    print(solve(1000))
    print(solve(150))
    print(sol