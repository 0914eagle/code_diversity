def solve(N):
    
    # your code here
    return bin(N).split('b')[1]

if __name__ == '__main__':
    print("Example:")
    print(solve(1000))
    print(solve